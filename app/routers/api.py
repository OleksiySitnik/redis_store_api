from fastapi import APIRouter, Depends, status

from app.dependencies import get_store_repository
from app.repositories.store_repository import AbstractStoreRepository
from app.routers.request_objects import (
    SetValueRequestObject,
    IncrementValueRequestObject,
)
from app.services.store_service import StoreService

router = APIRouter(prefix="/api/v1/store")


@router.post("/{key}", status_code=status.HTTP_201_CREATED)
async def set_value(
    key: str,
    body: SetValueRequestObject,
    store_repo: AbstractStoreRepository = Depends(get_store_repository),
):
    store_repo.set(key, body.value)
    return {"status": "success", "data": {"message": "Value set successfully"}}


@router.get("/{key}", status_code=status.HTTP_200_OK)
async def get_value(
    key: str,
    store_repo: AbstractStoreRepository = Depends(get_store_repository),
):
    value = store_repo.get(key)
    return {"status": "success", "data": {"value": value}}


@router.get("/{key}/exists", status_code=status.HTTP_200_OK)
async def key_exists(
    key: str,
    store_repo: AbstractStoreRepository = Depends(get_store_repository),
):
    exists = store_repo.exists(key)
    return {"status": "success", "data": {"exists": exists}}


@router.delete("/{key}", status_code=status.HTTP_200_OK)
async def delete_key(
    key: str,
    store_repo: AbstractStoreRepository = Depends(get_store_repository),
):
    store_repo.delete(key)
    return {"status": "success", "data": {"message": "Key deleted successfully"}}


@router.put("/{key}/increment", status_code=status.HTTP_200_OK)
async def increment_by(
    key: str,
    body: IncrementValueRequestObject,
    store_service: StoreService = Depends(StoreService),
):
    new_value = store_service.increment_by(key, body.increment)
    return {"status": "success", "data": {"new_value": new_value}}
