from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def route_root():
    return {
        "service": "fastapi-example",
        "version": "0.1.0",
    }
