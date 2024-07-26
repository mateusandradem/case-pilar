import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "order,expected_list", [("asc", ["batman", "coringa", "robin"]), ("desc", ["robin", "coringa", "batman"])]
)
def test_sort_words(order, expected_list):
    words_json = {"words": ["batman", "robin", "coringa"], "order": order}
    response = client.post("/sort/", json=words_json)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_list


def test_sort_words_wrong_payload():
    words_json = ["batman", "robin", "coringa"]
    response = client.post("/sort/", json=words_json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    "method",
    [client.get, client.head, client.put, client.patch, client.delete, client.options],
)
def test_count_vowels_method_not_allowed(method):
    response = method("/sort/")

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED