import uuid

from app.models import Incident

incidents_store = []


def detect_incident(metric):
    incidents = []

    if metric.cpu_usage >= 90:
        incidents.append({
            "severity": "CRITICAL",
            "issue": "High CPU Usage",
            "recommendation": "Investigate running processes and scale resources."
        })

    if metric.memory_usage >= 90:
        incidents.append({
            "severity": "CRITICAL",
            "issue": "High Memory Usage",
            "recommendation": "Check memory leaks and optimize applications."
        })

    if metric.disk_usage >= 90:
        incidents.append({
            "severity": "CRITICAL",
            "issue": "Low Disk Space",
            "recommendation": "Clean up storage or increase disk capacity."
        })

    return incidents


def create_incidents(metric):
    detected = detect_incident(metric)

    for item in detected:
        incident = Incident(
            incident_id=str(uuid.uuid4())[:8],
            server_name=metric.server_name,
            issue=item["issue"],
            severity=item["severity"],
            status="OPEN",
            recommendation=item["recommendation"]
        )

        incidents_store.append(incident)

    return incidents_store


def get_open_incidents():
    return [i for i in incidents_store if i.status == "OPEN"]


def resolve_incident(incident_id):
    for incident in incidents_store:
        if incident.incident_id == incident_id:
            incident.status = "RESOLVED"
            return incident

    return None
