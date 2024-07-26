import pytest

from src.service.sort_words_service import SortWordsService


@pytest.mark.parametrize(
    "order,expected_list", [("asc", ["batman", "coringa", "robin"]), ("desc", ["robin", "coringa", "batman"])]
)
def test_sort_words_service(order, expected_list):
    service = SortWordsService(["batman", "robin", "coringa"], order)

    assert service.sort_words() == expected_list
