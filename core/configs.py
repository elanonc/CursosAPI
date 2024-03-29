from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

class Settings(BaseSettings):
    """
        Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/cursos"
    DBBaseModel: DeclarativeMeta = declarative_base()

    class Config:
        case_sensitive: True

settings = Settings()