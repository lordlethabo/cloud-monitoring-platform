import platform
import psutil
from datetime import datetime


def get_system_health():
    return {
        "status": "Healthy",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "boot_time": datetime.fromtimestamp(
            psutil.boot_time()
        ).strftime("%Y-%m-%d %H:%M:%S"),
    }
