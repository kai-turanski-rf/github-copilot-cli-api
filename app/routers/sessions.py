from fastapi import APIRouter, Query

from app import database

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("")
def create_session() -> dict[str, str]:
    session = database.create_session()
    return {"message": "Session created", "session_id": str(session.id)}


@router.get("")
def get_recent_sessions(limit: int = Query(default=10, ge=1, le=100)) -> list[dict[str, str]]:
    sessions = database.get_recent_sessions(limit)
    return [{"id": str(session.id), "time_started": session.time_started.isoformat()} for session in sessions]