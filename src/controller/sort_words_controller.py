from fastapi import APIRouter

from ..service.sort_words_service import SortWordsService
from .models import WordsOrder

router = APIRouter(tags=["sort_words"])


@router.post("/v1/sort", description="Sort words in a given order")
def sort_words(words_order: WordsOrder):
    service = SortWordsService(**words_order.model_dump())

    return service.sort_words()
