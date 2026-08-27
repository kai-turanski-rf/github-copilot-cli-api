# GitHub Copilot API

FastAPI app, optionally backed by a containerized Postgres 18 database.

## Prerequisites

- Python 3.11+

## Setup

1. Copy the environment file:

   ```bash
   cp .env.example .env
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   python -m app.main
   ```

## Test

- Endpoint: http://localhost:8000/api/v1/test
- Docs: http://localhost:8000/docs

## Notes

#### Persistent sessions

By default the app does not store session IDs and creates a new session each time you hit the chat endpoint. This behaviour can be changed by setting up the Postgres DB and altering a line in [`chat.py`](<./app/routers/chat.py#L20>).

To setup Postgres you will need to use Docker and run:

```bash
docker compose up -d
```

Then execute the *CREATE TABLE* command in [database.py](<./app/database.py#L7>)