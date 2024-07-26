from typing import List

from pydantic import BaseModel


class WordsList(BaseModel):
    words: List[str]


class WordsOrder(WordsList):
    order: str
