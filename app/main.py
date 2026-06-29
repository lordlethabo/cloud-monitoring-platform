from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import create_tables, get_db
from app import crud, schemas
from app.monitoring import collect_metrics
from app.incidents import detect_incidents
from app.health import get_system_health
from app.settings import settings


create_tables()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Cloud Monitoring & Incident Response Platform built with FastAPI, SQLite, and Python."
)


@app.get("/")
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return get_system_health()


@app.post("/servers", response_model=schemas.ServerResponse)
def create_server(server: schemas.ServerCreate, db: Session = Depends(get_db)):
    existing_server = crud.get_server_by_server_id(db, server.server_id)

    if existing_server:
        raise HTTPException(
            status_code=400,
            detail="Server already exists."
        )

    return crud.create_server(db, server)


@app.get("/servers", response_model=list[schemas.ServerResponse])
def list_servers(db: Session = Depends(get_db)):
    return crud.get_servers(db)


@app.get("/metrics", response_model=list[schemas.MetricResponse])
def list_metrics(db: Session = Depends(get_db)):
    return crud.get_metrics(db)


@app.post("/scan/{server_id}")
def scan_server(server_id: str, db: Session = Depends(get_db)):
    server = crud.get_server_by_server_id(db, server_id)

    if server is None:
        raise HTTPException(
            status_code=404,
            detail="Server not found. Register the server first."
        )

    metric = collect_metrics(server_id)
    saved_metric = crud.create_metric(db, metric)

    detected_incidents = detect_incidents(metric)
    saved_incidents = []

    for incident in detected_incidents:
        saved_incident = crud.create_incident(db, incident)
        saved_incidents.append(saved_incident)

    return {
        "message": "Server scan completed successfully.",
        "metric": saved_metric,
        "incidents_created": len(saved_incidents),
        "incidents": saved_incidents
    }


@app.get("/incidents", response_model=list[schemas.IncidentResponse])
def list_incidents(db: Session = Depends(get_db)):
    return crud.get_incidents(db)


@app.get("/incidents/open", response_model=list[schemas.IncidentResponse])
def list_open_incidents(db: Session = Depends(get_db)):
    return crud.get_open_incidents(db)


@app.post("/incidents/{incident_id}/resolve", response_model=schemas.IncidentResponse)
def resolve_incident(incident_id: str, db: Session = Depends(get_db)):
    incident = crud.resolve_incident(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found."
        )

    return incident


@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    servers = crud.get_servers(db)
    incidents = crud.get_incidents(db)
    open_incidents = crud.get_open_incidents(db)
    metrics = crud.get_metrics(db)

    return {
        "total_servers": len(servers),
        "total_metrics": len(metrics),
        "total_incidents": len(incidents),
        "open_incidents": len(open_incidents),
        "healthy_servers": len([s for s in servers if s.status == "HEALTHY"]),
        "warning_servers": len([s for s in servers if s.status == "WARNING"]),
        "critical_servers": len([s for s in servers if s.status == "CRITICAL"])
    }
