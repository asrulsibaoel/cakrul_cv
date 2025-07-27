
from pydantic import BaseModel


class SkillCategoryCreate(BaseModel):
    name: str


class SkillCategory(BaseModel):
    id: int
    name: str
