from fastapi import APIRouter

from .models import WordsList
from ..service.vowels_counter_service import VowelsCounterService

router = APIRouter(tags=["words"])


@router.post("/vowel-count", description="Count vowels in words")
def count_vowels(words_list: WordsList):
    return VowelsCounterService().count_vowels([word for word in words_list.words])
