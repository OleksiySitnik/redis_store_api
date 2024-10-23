import pytest
from app.exceptions import KeyNotFoundException
from app.repositories.in_memory_store_repository import (
    InMemoryStoreRepository,
)


@pytest.fixture
def store_repo():
    return InMemoryStoreRepository()


def test_set_and_get(store_repo):
    store_repo.set("test_key", "test_value")
    assert store_repo.get("test_key") == "test_value"


def test_get_key_not_found(store_repo):
    with pytest.raises(KeyNotFoundException):
        store_repo.get("non_existing_key")


def test_delete_existing_key(store_repo):
    store_repo.set("key_to_delete", "value")
    assert store_repo.delete("key_to_delete") is True
    with pytest.raises(KeyNotFoundException):
        store_repo.get("key_to_delete")


def test_delete_non_existing_key(store_repo):
    assert store_repo.delete("non_existing_key") is False


def test_exists(store_repo):
    store_repo.set("existing_key", "some_value")
    assert store_repo.exists("existing_key") is True
    assert store_repo.exists("non_existing_key") is False
