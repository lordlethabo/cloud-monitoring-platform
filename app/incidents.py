from app.schemas import IncidentCreate
from app.recommendations import get_recommendation
from app.settings import settings
from app.utils import generate_incident_id


def detect_incidents(metric):
    incidents = []

    if metric.cpu_usage >= settings.CPU_CRITICAL:
        incidents.append(
            IncidentCreate(
                incident_id=generate_incident_id(),
                server_id=metric.server_id,
                issue="High CPU Usage",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("High CPU Usage")
            )
        )

    if metric.memory_usage >= settings.MEMORY_CRITICAL:
        incidents.append(
            IncidentCreate(
                incident_id=generate_incident_id(),
                server_id=metric.server_id,
                issue="High Memory Usage",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("High Memory Usage")
            )
        )

    if metric.disk_usage >= settings.DISK_CRITICAL:
        incidents.append(
            IncidentCreate(
                incident_id=generate_incident_id(),
                server_id=metric.server_id,
                issue="Low Disk Space",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("Low Disk Space")
            )
        )

    return incidents
