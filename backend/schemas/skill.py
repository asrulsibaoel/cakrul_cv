
from pydantic import BaseModel


class SkillCreate(BaseModel):
    name: str
    skill_category_id: int


class Skill(BaseModel):
    id: int
    name: str
    skill_category_id: int
