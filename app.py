from fastapi import FastAPI
from controllers import auth, test
from config import Env_settings

env_settings = Env_settings()

app = FastAPI(
    title=env_settings.title,
    version=env_settings.version
)

app.include_router(auth.router)
app.include_router(test.router)