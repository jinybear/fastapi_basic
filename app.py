from fastapi import FastAPI
from controllers import token, test
from config import Settings

settings = Settings()

app = FastAPI(
    title=settings.title,
    version=settings.version
)

app.include_router(token.router)
app.include_router(test.router)