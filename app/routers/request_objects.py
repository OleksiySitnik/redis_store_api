from pydantic import BaseModel


class SetValueRequestObject(BaseModel):
    value: str


class IncrementValueRequestObject(BaseModel):
    increment: int
