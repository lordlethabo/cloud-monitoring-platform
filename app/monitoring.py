import uuid
from datetime import datetime

import psutil

from app.models import Metric


def calculate_status(cpu: float, memory: float, disk: float) -> str:
    """
    Determine the overall health status of a server.
    """

    if cpu >= 90 or memory >= 90 or disk >= 90:
        return "CRITICAL"

    if cpu >= 75 or memory >= 75 or disk >= 75:
        return "WARNING"

    return "HEALTHY"


def collect_metrics(server_id: str):
    """
    Collect real system metrics from the machine.
    """

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    status = calculate_status(cpu, memory, disk)

    metric = Metric(
        metric_id=str(uuid.uuid4()),
        server_id=server_id,
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk,
        status=status,
        timestamp=datetime.now()
    )

    return metric


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent