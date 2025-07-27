
from pydantic import BaseModel
from typing import Optional


class EducationCreate(BaseModel):
    school_name: str
    title: str
    date_start: Optional[str] = None
    date_end: Optional[str] = None
    description: Optional[str] = None


class Education(BaseModel):
    id: int
    school_name: str
    title: str
    date_start: Optional[str]
    date_end: Optional[str]
    description: Optional[str]
