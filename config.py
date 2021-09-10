from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    version: str = "0"
    title: str = "fastapi_basic"

    class Config:
        env_file = os.getenv('RUN_MODE', '') + ".env"

