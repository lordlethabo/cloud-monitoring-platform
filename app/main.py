from fastapi import FastAPI, HTTPException

from app.models import Server
from app.monitoring import collect_metrics
from app.incidents import detect_incidents
from app.database import (
    save_server,
    get_servers,
    save_metric,
    get_metrics,
    save_incident,
    get_incidents,
    get_open_incidents,
    resolve_incident,
    get_dashboard_stats
)

app = FastAPI(
    title="Cloud Monitoring & Incident Response Platform",
    description="A cloud-native platform for monitoring servers, detecting incidents, and providing recommendations.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "Cloud Monitoring & Incident Response Platform",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/servers")
def create_server(server: Server):
    return save_server(server)


@app.get("/servers")
def list_servers():
    return get_servers()


@app.get("/metrics")
def list_metrics():
    return get_metrics()


@app.get("/metrics/{server_id}")
def collect_server_metrics(server_id: str):
    metric = collect_metrics(server_id)
    save_metric(metric)
    return metric


@app.post("/scan/{server_id}")
def scan_server(server_id: str):

    metric = collect_metrics(server_id)
    save_metric(metric)

    incidents = detect_incidents(metric)

    for incident in incidents:
        save_incident(incident)

    return {
        "message": "Server scan completed successfully.",
        "metric": metric,
        "incidents_created": len(incidents),
        "incidents": incidents
    }


@app.get("/incidents")
def list_incidents():
    return get_incidents()


@app.get("/incidents/open")
def list_open():
    return get_open_incidents()


@app.post("/incidents/{incident_id}/resolve")
def resolve(incident_id: str):

    incident = resolve_incident(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found."
        )

    return {
        "message": "Incident resolved successfully.",
        "incident": incident
    }


@app.get("/dashboard")
def dashboard():
    return get_dashboard_stats()
