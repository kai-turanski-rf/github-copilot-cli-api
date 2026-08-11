from fastapi import FastAPI
import uvicorn

app = FastAPI(title="GitHub Copilot API")


@app.get("/api/v1/test")
def test() -> dict[str, str]:
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")