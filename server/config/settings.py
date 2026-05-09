from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "XP Platform"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite:///./xp.db"
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str = "xp-secret-key-change-in-production-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
