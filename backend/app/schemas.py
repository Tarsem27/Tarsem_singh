from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ControlBase(BaseModel):
    framework: str = Field(min_length=2, max_length=64)
    title: str = Field(min_length=3, max_length=200)
    owner: str = Field(min_length=2, max_length=120)
    status: str = Field(default="todo", max_length=32)
    evidence_url: str | None = None
    is_critical: bool = False


class ControlCreate(ControlBase):
    pass


class Control(ControlBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
