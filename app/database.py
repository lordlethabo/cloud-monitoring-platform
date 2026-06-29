from typing import List
from app.models import Server, Metric, Incident

# In-memory databases
servers_db: List[Server] = []
metrics_db: List[Metric] = []
incidents_db: List[Incident] = []


def save_server(server: Server):
    """
    Save a new server.
    """
    servers_db.append(server)
    return server


def get_servers():
    """
    Return all registered servers.
    """
    return servers_db


def get_server(server_id: str):
    """
    Find a server by its ID.
    """
    for server in servers_db:
        if server.server_id == server_id:
            return server
    return None


def save_metric(metric: Metric):
    """
    Save collected metrics.
    """
    metrics_db.append(metric)
    return metric


def get_metrics():
    """
    Return all collected metrics.
    """
    return metrics_db


def get_server_metrics(server_id: str):
    """
    Return metrics for a specific server.
    """
    return [
        metric
        for metric in metrics_db
        if metric.server_id == server_id
    ]


def save_incident(incident: Incident):
    """
    Save a detected incident.
    """
    incidents_db.append(incident)
    return incident


def get_incidents():
    """
    Return all incidents.
    """
    return incidents_db


def get_open_incidents():
    """
    Return only open incidents.
    """
    return [
        incident
        for incident in incidents_db
        if incident.status == "OPEN"
    ]


def resolve_incident(incident_id: str):
    """
    Mark an incident as resolved.
    """
    for incident in incidents_db:
        if incident.incident_id == incident_id:
            incident.status = "RESOLVED"
            return incident

    return None


def delete_incident(incident_id: str):
    """
    Delete an incident.
    """
    global incidents_db

    for incident in incidents_db:
        if incident.incident_id == incident_id:
            incidents_db.remove(incident)
            return True

    return False


def get_dashboard_stats():
    """
    Return dashboard statistics.
    """

    total_servers = len(servers_db)
    total_metrics = len(metrics_db)
    total_incidents = len(incidents_db)

    healthy_servers = len([
        server for server in servers_db
        if server.status == "HEALTHY"
    ])

    warning_servers = len([
        server for server in servers_db
        if server.status == "WARNING"
    ])

    critical_servers = len([
        server for server in servers_db
        if server.status == "CRITICAL"
    ])

    open_incidents = len([
        incident
        for incident in incidents_db
        if incident.status == "OPEN"
    ])

    resolved_incidents = len([
        incident
        for incident in incidents_db
        if incident.status == "RESOLVED"
    ])

    return {
        "total_servers": total_servers,
        "healthy_servers": healthy_servers,
        "warning_servers": warning_servers,
        "critical_servers": critical_servers,
        "total_metrics": total_metrics,
        "total_incidents": total_incidents,
        "open_incidents": open_incidents,
        "resolved_incidents": resolved_incidents
    }
