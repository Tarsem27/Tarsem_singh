from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import Base, engine, get_db

app = FastAPI(title="OpenComply API", version="0.1.0")

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/controls", response_model=schemas.Control, status_code=201)
def create_control(payload: schemas.ControlCreate, db: Session = Depends(get_db)) -> models.Control:
    return crud.create_control(db, payload)


@app.get("/controls", response_model=list[schemas.Control])
def get_controls(framework: str | None = None, db: Session = Depends(get_db)) -> list[models.Control]:
    return crud.list_controls(db, framework=framework)
