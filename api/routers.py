from fastapi import APIRouter

from api.views import router as calculator_router


api_router = APIRouter()
api_router.include_router(calculator_router, prefix="/calculator", tags=["calculator"])
