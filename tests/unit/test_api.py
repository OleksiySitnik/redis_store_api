from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from app.dependencies import get_store_repository
from app.main import app
from app.services.store_service import StoreService

client = TestClient(app)


TEST_KEY = "test_key"
TEST_VALUE = "test_value"


class MockStoreRepo(MagicMock):
    set = MagicMock(return_value=None)
    get = MagicMock(return_value=TEST_VALUE)
    delete = MagicMock(return_value=None)
    exists = MagicMock(return_value=False)


class MockStoreService(MagicMock):
    increment_by = MagicMock(return_value=5)


def test_set_value():
    app.dependency_overrides[get_store_repository] = lambda: MockStoreRepo
    body = {"value": TEST_VALUE}

    response = client.post(f"/api/v1/store/{TEST_KEY}", json=body)
    assert response.status_code == 201
    assert response.json() == {
        "status": "success",
        "data": {"message": "Value set successfully"},
    }
    MockStoreRepo.set.assert_called_once_with(TEST_KEY, TEST_VALUE)

    app.dependency_overrides = {}


def test_get_value():
    app.dependency_overrides[get_store_repository] = lambda: MockStoreRepo

    response = client.get(f"/api/v1/store/{TEST_KEY}")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"value": TEST_VALUE}}
    MockStoreRepo.get.assert_called_once_with(TEST_KEY)

    app.dependency_overrides = {}


def test_key_exists():
    app.dependency_overrides[get_store_repository] = lambda: MockStoreRepo

    response = client.get(f"/api/v1/store/{TEST_KEY}/exists")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"exists": False}}
    MockStoreRepo.exists.assert_called_once_with(TEST_KEY)

    app.dependency_overrides = {}


def test_delete_key():
    app.dependency_overrides[get_store_repository] = lambda: MockStoreRepo

    response = client.delete(f"/api/v1/store/{TEST_KEY}")
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "data": {"message": "Key deleted successfully"},
    }
    MockStoreRepo.delete.assert_called_once_with(TEST_KEY)

    app.dependency_overrides = {}


def test_increment_by():
    app.dependency_overrides[StoreService] = lambda: MockStoreService

    response = client.put(f"/api/v1/store/{TEST_KEY}/increment", json={"increment": 5})
    assert response.status_code == 200
    assert response.json() == {"status": "success", "data": {"new_value": 5}}
    MockStoreService.increment_by.assert_called_once_with(TEST_KEY, 5)

    app.dependency_overrides = {}
