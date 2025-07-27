
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Certificate
from schemas import CertificateCreate

class CertificateRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_id(self, id: int) -> Certificate | None:
        return await self.db_session.get(Certificate, id)

    async def list_all(self) -> list[Certificate]:
        result = await self.db_session.execute(select(Certificate))
        return result.scalars().all()

    async def create(self, schema: CertificateCreate) -> Certificate:
        obj = Certificate(**schema.dict())
        self.db_session.add(obj)
        await self.db_session.commit()
        await self.db_session.refresh(obj)
        return obj

    async def delete(self, id: int) -> bool:
        obj = await self.get_by_id(id)
        if not obj:
            return False
        await self.db_session.delete(obj)
        await self.db_session.commit()
        return True
