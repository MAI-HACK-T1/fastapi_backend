# config.py
import os
from pathlib import Path
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, PostgresDsn
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

class LogConfig(BaseModel):
    """Конфигурация логирования"""
    LOGGER_NAME: str = "backend_app"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"
    
    # Пути к файлам логов
    LOG_PATH: str = str(BASE_DIR / "logs")
    ERROR_LOG_FILENAME: str = "error.log"
    INFO_LOG_FILENAME: str = "info.log"


class DatabaseConfig(BaseModel):
    """Конфигурация подключения к базе данных"""
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    
    @property
    def DATABASE_URL_asyncpg(self):
        # DSN
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    

class AuthJWT(BaseModel):
    PRIVATE_KEY_PATH: Path = BASE_DIR / "certs" / "jwt-private.pem"
    PUBLIC_KEY_PATH: Path = BASE_DIR / "certs" / "jwt-public.pem"
    ALRORITHMS: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "")
    REFRESH_TOKEN_EXPIRE_DAYS: int = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "")



class APIConfig(BaseModel):
    """Конфигурация API и внешних сервисов"""

    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "*").split(",")


class Settings(BaseModel):
    """Основной класс настроек, объединяющий все конфигурации"""


    # Подключаем конфигурации
    log: LogConfig = LogConfig()
    db: DatabaseConfig = DatabaseConfig()
    auth_jwt: AuthJWT = AuthJWT(    )
    api: APIConfig = APIConfig()
    

settings = Settings()

