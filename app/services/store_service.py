from app.dependencies import get_store_repository
from app.exceptions import KeyNotFoundException, InvalidKeyValueType


class StoreService:
    def __init__(self):
        self._store_repo = get_store_repository()

    def increment_by(self, key: str, increment: int) -> int:
        current_value = self._store_repo.get(key)
        if current_value is None:
            raise KeyNotFoundException(key=key)

        if not current_value.isdigit():
            raise InvalidKeyValueType(
                "Value is not an integer and cannot be incremented"
            )

        new_value = int(current_value) + increment
        self._store_repo.set(key, str(new_value))
        return new_value
