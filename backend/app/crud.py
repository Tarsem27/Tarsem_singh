from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def create_control(db: Session, payload: schemas.ControlCreate) -> models.Control:
    control = models.Control(**payload.model_dump())
    db.add(control)
    db.commit()
    db.refresh(control)
    return control


def list_controls(db: Session, framework: str | None = None) -> list[models.Control]:
    query = select(models.Control).order_by(models.Control.created_at.desc())
    if framework:
        query = query.where(models.Control.framework == framework)
    return list(db.scalars(query).all())
