from typing import List
from app.models import Server, Metric, Incident


servers_db: List[Server] = []
metrics_db: List[Metric] = []
incidents_db: List[Incident] = []


def save_server(server: Server):
    servers_db.append(server)
    return server


def get_servers():
    return servers_db


def save_metric(metric: Metric):
    metrics_db.append(metric)
    return metric


def get_metrics():
    return metrics_db


def save_incident(incident: Incident):
    incidents_db.append(incident)
    return incident


def get_incidents():
    return incidents_db


def get_open_incidents():
    return [
        incident for incident in incidents_db
        if incident.status == "OPEN"
    ]


def resolve_incident(incident_id: str):
    for incident in incidents_db:
        if incident.incident_id == incident_id:
            incident.status = "RESOLVED"
            return incident

    return None


def get_dashboard_stats():
    total_servers = len(servers_db)
    total_incidents = len(incidents_db)
    open_incidents = len(get_open_incidents())
    resolved_incidents = len([
        incident for incident in incidents_db
        if incident.status == "RESOLVED"
    ])

    return {
        "total_servers": total_servers,
        "total_metrics": len(metrics_db),
        "total_incidents": total_incidents,
        "open_incidents": open_incidents,
        "resolved_incidents": resolved_incidents
    }