from fastapi import APIRouter

from .controller.sort_words_controller import router as sort_router
from .controller.vowels_counter_controller import router as vowels_router

api_router = APIRouter()

api_router.include_router(vowels_router)
api_router.include_router(sort_router)
