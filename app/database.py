"""
Module for interacting with the local database.

DB Contents:

```
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT uuidv7(),
    time_started TIMESTAMP NOT NULL DEFAULT NOW(),
);
```
"""
from collections.abc import Generator
from datetime import datetime
from uuid import UUID

import psycopg
from psycopg.rows import class_row
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Session as SASession

from app.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[SASession, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Session(BaseModel):
    id: UUID
    time_started: datetime


def create_session() -> Session:
    with psycopg.connect(settings.database_url) as conn:
        with conn.cursor(row_factory=class_row(Session)) as cur:
            cur.execute(
                "INSERT INTO sessions DEFAULT VALUES RETURNING id, time_started"
            )
            return cur.fetchone()


def get_recent_sessions(limit: int = 10) -> list[Session]:
    with psycopg.connect(settings.database_url) as conn:
        with conn.cursor(row_factory=class_row(Session)) as cur:
            cur.execute(
                "SELECT id, time_started FROM sessions "
                "ORDER BY time_started DESC LIMIT %s",
                (limit,),
            )
            return cur.fetchall()