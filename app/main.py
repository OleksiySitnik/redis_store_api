from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import DetailedException
from app.routers import api

app = FastAPI()

app.include_router(api.router)


@app.get("/healthcheck")
def health_check():
    return {"status": "healthy"}


@app.exception_handler(DetailedException)
async def detailed_exception_handler(request: Request, exc: DetailedException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict(),
    )
