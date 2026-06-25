from fastapi import FastAPI

from app.monitoring import collect_metrics
from app.incidents import (
    create_incidents,
    get_open_incidents,
    resolve_incident
)

app = FastAPI(
    title="Cloud Monitoring Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Cloud Monitoring & Incident Response Platform"
    }


@app.get("/metrics")
def metrics():
    metric = collect_metrics()
    return metric


@app.post("/scan")
def scan():
    metric = collect_metrics()
    incidents = create_incidents(metric)

    return {
        "metric": metric,
        "incidents": incidents
    }


@app.get("/incidents")
def incidents():
    return get_open_incidents()


@app.post("/resolve/{incident_id}")
def resolve(incident_id: str):
    return resolve_incident(incident_id)
