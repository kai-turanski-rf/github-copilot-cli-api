# GitHub Copilot API

FastAPI app (runs locally) backed by a containerized Postgres 18 database.

## Prerequisites

- Python 3.11+
- Docker + Docker Compose

## Setup

1. Copy the environment file:

   ```bash
   cp .env.example .env
   ```

2. Start Postgres:

   ```bash
   docker compose up -d
   ```

3. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Run the API:

   ```bash
   uvicorn app.main:app --reload
   ```

## Test

- Endpoint: http://localhost:8000/api/v1/test
- Docs: http://localhost:8000/docs
