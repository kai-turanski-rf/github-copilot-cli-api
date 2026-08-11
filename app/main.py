from fastapi import FastAPI
import uvicorn

from app.routers import sessions

app = FastAPI(title="GitHub Copilot API")
app.include_router(sessions.router, prefix="/api/v1")


@app.get("/api/v1/test")
def test() -> dict[str, str]:
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
