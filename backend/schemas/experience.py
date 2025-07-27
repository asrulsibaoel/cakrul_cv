
from pydantic import BaseModel
from typing import Optional


class ExperienceCreate(BaseModel):
    company_name: str
    title: str
    date_start: Optional[str] = None
    date_end: Optional[str] = None
    description: Optional[str] = None


class Experience(BaseModel):
    id: int
    company_name: str
    title: str
    date_start: Optional[str]
    date_end: Optional[str]
    description: Optional[str]
