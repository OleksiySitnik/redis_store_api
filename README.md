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
 - **Integration**
    ```
    pytest -v tests/integration
    ```
 - **Unit**
    ```
    pytest -v tests/unit
   ```

### Manual Testing with Bash Script

``. test_api.sh``

## Feedback
 - Complexity: easy-medium

 - Time spent (total: 3-4h)
    - Setup and Initial Configuration: 30 min
    - Developing API Endpoints (including shell script): 1.5 hour
    - Writing Tests and Testing: ~1 hour
    - Docker: 30 hour
    - CI: 30-40 minutes
 
 The main challenge I faced with the task was understanding the project's real-world application, as real projects typically have a clear goal. It was unclear whether the aim was to replicate Redis functionality, create a unique API-driven database, or allow for integration with external databases instead of just using in-memory storage.

 In my implementation, I focused on placing logic within the repository, with some in the service layer, mimicking a real project's structure. While it might be possible to develop use cases for the API, I felt that would add unnecessary complexity at this stage.