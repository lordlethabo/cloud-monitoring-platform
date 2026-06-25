import psutil
from app.models import ServerMetric


def get_status(cpu, memory, disk):
    if cpu >= 90 or memory >= 90 or disk >= 90:
        return "CRITICAL"

    if cpu >= 75 or memory >= 75 or disk >= 75:
        return "WARNING"

    return "HEALTHY"


def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    metric = ServerMetric(
        server_id="srv-001",
        server_name="cloud-server",
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk,
        status=get_status(cpu, memory, disk)
    )

    return metric
