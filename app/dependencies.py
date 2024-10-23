from app.repositories.in_memory_store_repository import InMemoryStoreRepository
from app.repositories.store_repository import AbstractStoreRepository

in_memory_store_repository = InMemoryStoreRepository()


def get_store_repository() -> AbstractStoreRepository:
    return in_memory_store_repository
