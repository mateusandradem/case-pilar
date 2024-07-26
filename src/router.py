from fastapi import APIRouter

from .controller.vowels_counter_controller import router as vowels_router

api_router = APIRouter()

api_router.include_router(vowels_router)
