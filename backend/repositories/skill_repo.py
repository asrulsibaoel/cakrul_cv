
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Skill
from schemas import SkillCreate


class SkillRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_id(self, id: int) -> Skill | None:
        return await self.db_session.get(Skill, id)

    async def list_all(self) -> list[Skill]:
        result = await self.db_session.execute(select(Skill))
        return result.scalars().all()

    async def create(self, schema: SkillCreate) -> Skill:
        obj = Skill(**schema.dict())
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
