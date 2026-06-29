import os


class Settings:

    APP_NAME = "Cloud Monitoring & Incident Response Platform"

    APP_VERSION = "1.0.0"

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    HOST = os.getenv("HOST", "0.0.0.0")

    PORT = int(os.getenv("PORT", "8000"))

    CPU_WARNING = int(os.getenv("CPU_WARNING", "80"))
    CPU_CRITICAL = int(os.getenv("CPU_CRITICAL", "90"))

    MEMORY_WARNING = int(os.getenv("MEMORY_WARNING", "80"))
    MEMORY_CRITICAL = int(os.getenv("MEMORY_CRITICAL", "90"))

    DISK_WARNING = int(os.getenv("DISK_WARNING", "80"))
    DISK_CRITICAL = int(os.getenv("DISK_CRITICAL", "90"))


settings = Settings()
