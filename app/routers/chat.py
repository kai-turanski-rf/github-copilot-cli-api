from fastapi import APIRouter
from pydantic import BaseModel, Field

from app import cli_connect, database

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    system_prompt: str | None = Field(default=None, min_length=1, max_length=1000)
    user_prompt: str = Field(min_length=1, max_length=1000)


@router.post("")
def get_completion(request: ChatRequest) -> dict[str, str]:
    session = database.create_session()

    if request.system_prompt:
        prompt = build_prompt(request.system_prompt, request.user_prompt)
    else:
        prompt = request.user_prompt

    try:
        completion = cli_connect.get_copilot_completion(prompt, session.id)
    except Exception as e:
        print(f"Error getting completion: {e}")
        return {"error": "Error getting completion.", "session_id": str(session.id)}

    return {"data": str(completion), "session_id": str(session.id)}


def build_prompt(system_prompt: str, user_prompt: str) -> str:
    """Build the prompt to send to GitHub Copilot."""
    return f"<SYSTEM_PROMPT>{system_prompt}</SYSTEM_PROMPT>\n<USER_PROMPT>{user_prompt}</USER_PROMPT>"