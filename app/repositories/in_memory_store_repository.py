from typing import Dict

from app.exceptions import KeyNotFoundException
from app.repositories.store_repository import AbstractStoreRepository


class InMemoryStoreRepository(AbstractStoreRepository):
    def __init__(self):
        self._store: Dict[str, str] = {}

    def set(self, key: str, value: str) -> None:
        self._store[key] = value

    def get(self, key: str) -> str:
        value = self._store.get(key)
        if value is None:
            raise KeyNotFoundException(key)

        return value

    def delete(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False

    def exists(self, key: str) -> bool:
        return key in self._store
