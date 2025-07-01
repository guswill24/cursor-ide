from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Información del proyecto
    project_name: str = "platziflix-backend"
    version: str = "0.1.0"
    
    # Configuración de base de datos
    database_url: str = "postgresql://user:password@localhost:5432/platziflix"
    
    # Configuración del servidor
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Configuración adicional
    debug: bool = False
    
    model_config = SettingsConfigDict(env_file=".env")


# Función para obtener settings con caché
from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    return Settings()
