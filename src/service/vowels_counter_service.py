from collections import Counter

VOWELS = set("aeiou")


class VowelsCounterService:
    @classmethod
    def count_vowels(cls, words: list[str]) -> dict[str]:
        words_vowels = Counter()

        for word in words:
            for letter in word.lower():
                if letter in VOWELS:
                    words_vowels[word] += 1

        return dict(words_vowels)
