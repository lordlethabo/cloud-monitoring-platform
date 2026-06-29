import uuid
from datetime import datetime


def generate_server_id():
    return f"SRV-{uuid.uuid4().hex[:8].upper()}"


def generate_metric_id():
    return f"MET-{uuid.uuid4().hex[:8].upper()}"


def generate_incident_id():
    return f"INC-{uuid.uuid4().hex[:8].upper()}"


def current_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
