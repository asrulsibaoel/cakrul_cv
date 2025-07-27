
from pydantic import BaseModel


class InterestCreate(BaseModel):
    name: str


class Interest(BaseModel):
    id: int
    name: str
