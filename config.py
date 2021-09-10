from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    revision: str = "0"
    title: str = "ITU_LOG_AGENT"

    class Config:
        env_file = os.getenv('RUN_MODE', '') + ".env"

