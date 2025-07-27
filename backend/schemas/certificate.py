
from pydantic import BaseModel
from typing import Optional


class CertificateCreate(BaseModel):
    issuer: str
    title: str
    icon_url: Optional[str] = None
    description: Optional[str] = None


class Certificate(BaseModel):
    id: int
    issuer: str
    title: str
    icon_url: Optional[str]
    description: Optional[str]
