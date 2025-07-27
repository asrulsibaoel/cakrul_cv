
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Experience
from schemas import ExperienceCreate

class ExperienceRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_id(self, id: int) -> Experience | None:
        return await self.db_session.get(Experience, id)

    async def list_all(self) -> list[Experience]:
        result = await self.db_session.execute(select(Experience))
        return result.scalars().all()

    async def create(self, schema: ExperienceCreate) -> Experience:
        obj = Experience(**schema.dict())
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
