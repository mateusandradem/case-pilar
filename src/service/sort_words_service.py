class SortWordsService:
    def __init__(self, words, order):
        self.words = words
        self.order = order

    def sort_words(self) -> list[str]:
        return sorted(self.words, reverse=self.order == "desc")
