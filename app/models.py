from pydantic import BaseModel


class ServerMetric(BaseModel):
    server_id: str
    server_name: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    status: str


class Incident(BaseModel):
    incident_id: str
    server_name: str
    issue: str
    severity: str
    status: str
    recommendation: str
