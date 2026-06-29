from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./cloud_monitoring.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def create_tables():
    from app.models import Server, Metric, Incident
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()    """
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
