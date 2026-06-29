from datetime import datetime
from pydantic import BaseModel


class ServerCreate(BaseModel):
    server_id: str
    server_name: str
    ip_address: str
    operating_system: str
    status: str = "UNKNOWN"


class ServerResponse(ServerCreate):
    id: int

    class Config:
        from_attributes = True


class MetricCreate(BaseModel):
    metric_id: str
    server_id: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    status: str


class MetricResponse(MetricCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class IncidentCreate(BaseModel):
    incident_id: str
    server_id: str
    issue: str
    severity: str
    status: str = "OPEN"
    recommendation: str


class IncidentResponse(IncidentCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
