from src.service.vowels_counter_service import VowelsCounterService


def test_count_vowels():
    words = ["batman", "robin", "coringa"]
    expected_count = {"batman": 2, "robin": 2, "coringa": 3}

    assert VowelsCounterService.count_vowels(words) == expected_count
