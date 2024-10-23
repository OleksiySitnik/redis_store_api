class DetailedException(Exception):
    def __init__(
        self,
        debug_message: str,
        status_code: int = 400,
        payload: dict = None,
    ):
        self.status_code = status_code
        self.debug_message = debug_message
        self.payload = payload

    def to_dict(self):
        return {
            "status": "error",
            **(self.payload or {}),
            "message": self.debug_message,
        }


class KeyNotFoundException(DetailedException):
    def __init__(self, key: str):
        super().__init__(
            debug_message=f"Key '{key}' not found",
            status_code=404,
        )


class InvalidKeyValueType(DetailedException):
    def __init__(self, message: str):
        super().__init__(
            debug_message=message or "Invalid value type",
        )
