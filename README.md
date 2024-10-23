# Key/Value Store api

## Project Structure

### `app/`
- **repositories/**: Implements the data access layer.
  - `in_memory_store_repository.py`: In-memory data storage logic.
  - `store_repository.py`: Abstract base class for data storage.
- **routers/**: Handles API routing.
  - `api.py`: Defines endpoints.
  - `request_objects.py`: Request validation models.
- **services/**: Business logic layer.
  - `store_service.py`: Manages business logic, such as value incrementation.
- `dependencies.py`: Manages dependency injection.
- `exceptions.py`: Custom exception classes for error handling.

### `tests/`
- **integration/**
  - contain integration tests
- **unit/**
  - contain unit tests

### Running the Application with Docker

```bash
docker-compose up --build
```

## Setup

Follow these steps to get your application up and running locally:

1. **Install Dependencies:**

   ```bash
   pipenv install
   ```
2. **Activate virtualenv:**
    ```bash
   pipenv shell
   ```

3. **Run the Application:**
    ```bash
   uvicorn app.main:app --reload
   ```

### Running tests
 - ###Integration
    `pytest -v tests/integration`
 - ###Unit
    `pytest -v tests/unit`

### Manual Testing with Bash Script

``. test_api.sh``
