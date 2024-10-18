# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
# Example Logging Setup
import logging

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    MYSQL_DATABASE: str = Field(..., env="MYSQL_DATABASE")
    MYSQL_USER: str = Field(..., env="MYSQL_USER")
    MYSQL_PASSWORD: str = Field(..., env="MYSQL_PASSWORD")
    MYSQL_ROOT_PASSWORD: str = Field(..., env="MYSQL_ROOT_PASSWORD")
    API_KEY: Optional[str] = Field(None, env="API_KEY")  # Optional API_KEY

    class Config:
        env_file = ".env"

settings = Settings()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)