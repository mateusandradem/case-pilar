from fastapi import APIRouter

from ..service.vowels_counter_service import VowelsCounterService
from .models import WordsList

router = APIRouter(tags=["words"])


@router.post("/vowel-count", description="Count vowels in words")
def count_vowels(words_list: WordsList):
    return VowelsCounterService.count_vowels([word for word in words_list.words])
