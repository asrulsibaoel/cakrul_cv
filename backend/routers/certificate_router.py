
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from database import get_async_session
from models import User
from repositories.certificate_repo import CertificateRepository
from schemas import CertificateCreate, Certificate

router = APIRouter(prefix="/certificate", tags=["certificate"])


@router.post("/", response_model=Certificate)
async def create_item(
    schema: CertificateCreate,
    db_session: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user),
):
    repo = CertificateRepository(db_session)
    return await repo.create(schema)


@router.get("/", response_model=list[Certificate])
async def list_items(
    db_session: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user),
):
    repo = CertificateRepository(db_session)
    return await repo.list_all()


@router.delete("/{item_id}/")
async def delete_item(
    item_id: int,
    db_session: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user),
):
    repo = CertificateRepository(db_session)
    success = await repo.delete(item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Certificate with id {item_id} not found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
