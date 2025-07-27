
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Languages
from schemas import LanguageCreate

class LanguageRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_id(self, id: int) -> Languages | None:
        return await self.db_session.get(Languages, id)

    async def list_all(self) -> list[Languages]:
        result = await self.db_session.execute(select(Languages))
        return result.scalars().all()

    async def create(self, schema: LanguageCreate) -> Languages:
        obj = Languages(**schema.dict())
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
