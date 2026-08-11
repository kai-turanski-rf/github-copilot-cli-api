from fastapi import APIRouter
from pydantic import BaseModel, Field

from app import cli_connect, database

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=500)


@router.post("")
def get_completion(request: ChatRequest) -> dict[str, str]:
    session = database.create_session()

    try:
        completion = cli_connect.get_copilot_completion(request.prompt, session.id)
    except Exception as e:
        print(f"Error getting completion: {e}")
        return {"error": "Error getting completion.", "session_id": str(session.id)}

    return {"data": str(completion), "session_id": str(session.id)}
