from sqlalchemy import Column, DateTime, Float, Integer, String
from datetime import datetime

from app.database import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(String, unique=True, index=True, nullable=False)
    server_name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    operating_system = Column(String, nullable=False)
    status = Column(String, default="UNKNOWN")


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    metric_id = Column(String, unique=True, index=True, nullable=False)
    server_id = Column(String, index=True, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_usage = Column(Float, nullable=False)
    disk_usage = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(String, unique=True, index=True, nullable=False)
    server_id = Column(String, index=True, nullable=False)
    issue = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, default="OPEN")
    recommendation = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
