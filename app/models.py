from pydantic import BaseModel
from datetime import datetime


class Server(BaseModel):
    server_id: str
    server_name: str
    ip_address: str
    operating_system: str
    status: str


class Metric(BaseModel):
    metric_id: str
    server_id: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    status: str
    timestamp: datetime


class Incident(BaseModel):
    incident_id: str
    server_id: str
    issue: str
    severity: str
    status: str
    recommendation: str
    timestamp: datetime