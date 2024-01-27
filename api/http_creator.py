import uvicorn
from mangum import Mangum
from fastapi import FastAPI

fastAPI_app = FastAPI(
    title="Book Store API",
    description="Book Store API",
    version="0.0.1",
)


@fastAPI_app.get("/v1/books")
def list_books():
    return {
        'message': 'No books yet :('
    }


handler = Mangum(fastAPI_app, lifespan="off")

if __name__ == "__main__":
    uvicorn.run(
        fastAPI_app,
        port=8099,
        log_level="debug",
    )