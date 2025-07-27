from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    email: str
    username: str
    password: str
    brithday: str
    phone: str
    address: str
    created_at: datetime


class UserCreate(BaseModel):
    name: str
    email: str
    username: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    created_at: datetime
