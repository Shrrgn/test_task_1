from fastapi import FastAPI

from api.config import settings
from api.routers import api_router

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    description=settings.description,
)
app.include_router(api_router)
