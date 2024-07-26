import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_count_vowels():
    words_json = {"words": ["batman", "robin", "coringa"]}
    response = client.post("/v1/vowel-count/", json=words_json)
    expected_count = {"batman": 2, "robin": 2, "coringa": 3}

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_count


def test_count_vowels_wrong_payload():
    words_json = ["batman", "robin", "coringa"]
    response = client.post("/v1/vowel-count/", json=words_json)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    "method",
    [client.get, client.head, client.put, client.patch, client.delete, client.options],
)
def test_count_vowels_method_not_allowed(method):
    response = method("/v1/vowel-count/")

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
