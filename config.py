import os
import json
from pydantic import BaseSettings

class Env_settings(BaseSettings):
    version: str = "0"
    title: str = "fastapi_basic"

    class Config:
        env_file = os.getenv('RUN_MODE', '') + ".env"

class Oper_settings():
    def __init__(self):
        self.setting = None
        self.load()

    def load(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        SETTINGS_PATH = '/'.join([dir_path, 'setting.json'])

        with open(SETTINGS_PATH, 'r') as f:
            self.setting = json.load(f)

oper_settings = Oper_settings()


