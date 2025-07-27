
from pydantic import BaseModel


class LanguageCreate(BaseModel):
    language_name: str
    level: str


class Languages(BaseModel):
    id: int
    language_name: str
    level: str
