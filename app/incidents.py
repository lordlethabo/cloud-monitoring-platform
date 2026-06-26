import uuid
from datetime import datetime

from app.models import Incident
from app.recommendations import get_recommendation


def detect_incidents(metric):
    incidents = []

    if metric.cpu_usage >= 90:
        incidents.append(
            Incident(
                incident_id=str(uuid.uuid4()),
                server_id=metric.server_id,
                issue="High CPU Usage",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("High CPU Usage"),
                timestamp=datetime.now()
            )
        )

    if metric.memory_usage >= 90:
        incidents.append(
            Incident(
                incident_id=str(uuid.uuid4()),
                server_id=metric.server_id,
                issue="High Memory Usage",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("High Memory Usage"),
                timestamp=datetime.now()
            )
        )

    if metric.disk_usage >= 90:
        incidents.append(
            Incident(
                incident_id=str(uuid.uuid4()),
                server_id=metric.server_id,
                issue="Low Disk Space",
                severity="CRITICAL",
                status="OPEN",
                recommendation=get_recommendation("Low Disk Space"),
                timestamp=datetime.now()
            )
        )

    return incidents