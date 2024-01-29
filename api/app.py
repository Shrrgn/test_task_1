from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from api.config import settings
from api.routers import api_router

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    description=settings.description,
)
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def calculator(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
