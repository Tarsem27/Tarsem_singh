# OpenComply Starter (Free & Self-Hosted)

This repository now includes a subscription-free starter for a compliance tracking app similar in spirit to CompliantPro.

## What is included

- FastAPI backend with basic control tracking endpoints
- PostgreSQL for structured data
- MinIO for evidence/document storage (S3-compatible)
- Docker Compose for local self-hosted setup
- Basic API tests with pytest

## Project structure

- `backend/app/main.py` - API routes
- `backend/app/models.py` - SQLAlchemy models
- `backend/app/schemas.py` - request/response schemas
- `backend/app/crud.py` - data access logic
- `backend/tests/test_api.py` - API smoke tests
- `docker-compose.yml` - local stack (API + Postgres + MinIO)

## Quick start

### 1) Run full stack with Docker Compose

```bash
docker compose up --build
```

Services:

- API: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- MinIO API: `http://localhost:9000`
- MinIO Console: `http://localhost:9001`

### 2) Example API usage

Create a control:

```bash
curl -X POST http://localhost:8000/controls \
  -H "Content-Type: application/json" \
  -d '{
    "framework": "SOC2",
    "title": "Enable MFA for admin accounts",
    "owner": "Security",
    "status": "in_progress",
    "is_critical": true
  }'
```

List controls:

```bash
curl "http://localhost:8000/controls?framework=SOC2"
```

## Local development (without Docker)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

By default this mode uses SQLite (`compliance.db`).

## Run tests

```bash
cd backend
pytest
```

## Next recommended steps

1. Add authentication (JWT + RBAC)
2. Add organizations/multi-tenancy
3. Integrate MinIO uploads for evidence attachments
4. Add framework templates (SOC 2, ISO 27001)
5. Add audit log table and report exports
