from fastapi import FastAPI
from src.routers.mongodb_tester import router as mongodb_router

app = FastAPI()


@app.get("/")
def route_root() -> dict:
    return {
        "service": "tests-private",
        "version": "0.1.0",
        "tests": True,
    }


app.include_router(mongodb_router, prefix="/mongodb", tags=["mongodb"])
