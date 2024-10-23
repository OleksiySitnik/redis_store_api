import httpx
import pytest

BASE_URL = "http://127.0.0.1:8000/api/v1/store"

TEST_KEY = "test_key"
TEST_VALUE = "test_value"


@pytest.mark.asyncio
async def test_set_and_get_value():
    async with httpx.AsyncClient() as client:
        body = {"value": TEST_VALUE}

        response = await client.post(f"{BASE_URL}/{TEST_KEY}", json=body)

        assert response.status_code == 201
        assert response.json() == {
            "status": "success",
            "data": {"message": "Value set successfully"},
        }

        response = await client.get(f"{BASE_URL}/{TEST_KEY}")

        assert response.status_code == 200
        assert response.json() == {"status": "success", "data": {"value": TEST_VALUE}}


@pytest.mark.asyncio
async def test_set_and_delete_value():
    async with httpx.AsyncClient() as client:
        body = {"value": TEST_VALUE}

        response = await client.post(f"{BASE_URL}/{TEST_KEY}", json=body)

        assert response.status_code == 201
        assert response.json() == {
            "status": "success",
            "data": {"message": "Value set successfully"},
        }

        response = await client.delete(f"{BASE_URL}/{TEST_KEY}")

        assert response.status_code == 200
        assert response.json() == {
            "status": "success",
            "data": {"message": "Key deleted successfully"},
        }

        response = await client.get(f"{BASE_URL}/{TEST_KEY}/exists")

        assert response.status_code == 200
        assert response.json() == {"status": "success", "data": {"exists": False}}
