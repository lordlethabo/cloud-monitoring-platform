import psutil

from app.schemas import MetricCreate
from app.utils import generate_metric_id
from app.settings import settings


def calculate_status(cpu_usage: float, memory_usage: float, disk_usage: float) -> str:
    if (
        cpu_usage >= settings.CPU_CRITICAL
        or memory_usage >= settings.MEMORY_CRITICAL
        or disk_usage >= settings.DISK_CRITICAL
    ):
        return "CRITICAL"

    if (
        cpu_usage >= settings.CPU_WARNING
        or memory_usage >= settings.MEMORY_WARNING
        or disk_usage >= settings.DISK_WARNING
    ):
        return "WARNING"

    return "HEALTHY"


def collect_metrics(server_id: str) -> MetricCreate:
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    status = calculate_status(
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_usage=disk_usage
    )

    return MetricCreate(
        metric_id=generate_metric_id(),
        server_id=server_id,
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_usage=disk_usage,
        status=status
    )
