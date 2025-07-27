from datetime import date, datetime
from pydantic import BaseModel


class CreateTaskSchema(BaseModel):
    text: str
    priority: int
    posted_at: date


class TasksByDateSchema(BaseModel):
    date: date


class UpdateTaskSchema(BaseModel):
    priority: int | None = None
    text: str | None = None
    completed: bool | None = None


class UpdateTaskPrioritiesSchema(BaseModel):
    """id:priority dictionary to update"""

    priorities: dict[int, int]


class DisplayTaskSchema(BaseModel):
    id: int
    priority: int
    text: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
