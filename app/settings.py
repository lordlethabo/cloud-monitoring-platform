from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Cloud Monitoring & Incident Response Platform"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = False

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    CPU_WARNING: int = 80
    CPU_CRITICAL: int = 90

    MEMORY_WARNING: int = 80
    MEMORY_CRITICAL: int = 90

    DISK_WARNING: int = 80
    DISK_CRITICAL: int = 90

    class Config:
        env_file = ".env"


settings = Settings()
