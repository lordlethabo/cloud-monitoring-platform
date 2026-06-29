from sqlalchemy.orm import Session

from app import models, schemas


def create_server(db: Session, server: schemas.ServerCreate):
    db_server = models.Server(**server.model_dump())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server


def get_servers(db: Session):
    return db.query(models.Server).all()


def get_server_by_server_id(db: Session, server_id: str):
    return db.query(models.Server).filter(
        models.Server.server_id == server_id
    ).first()


def create_metric(db: Session, metric: schemas.MetricCreate):
    db_metric = models.Metric(**metric.model_dump())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric


def get_metrics(db: Session):
    return db.query(models.Metric).order_by(
        models.Metric.timestamp.desc()
    ).all()


def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_incidents(db: Session):
    return db.query(models.Incident).order_by(
        models.Incident.timestamp.desc()
    ).all()


def get_open_incidents(db: Session):
    return db.query(models.Incident).filter(
        models.Incident.status == "OPEN"
    ).order_by(
        models.Incident.timestamp.desc()
    ).all()


def resolve_incident(db: Session, incident_id: str):
    incident = db.query(models.Incident).filter(
        models.Incident.incident_id == incident_id
    ).first()

    if incident is None:
        return None

    incident.status = "RESOLVED"
    db.commit()
    db.refresh(incident)
    return incident
