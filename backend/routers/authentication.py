from datetime import timedelta
from typing import TYPE_CHECKING

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from auth import create_access_token, create_refresh_token
from config import settings
from database import get_async_session
from repositories.user_repo import UserRepository
from schemas import RefreshTokenSchema

if TYPE_CHECKING:
    from models import User


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/jwt/create/")
async def login(
    db_session: AsyncSession = Depends(get_async_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    ## LogIn a User
    This requires the following fields:
    ```
        username: str
        password: str

    and returns a token pair 'access' and 'refresh' tokens
    ```

    """
    user_repo = UserRepository(db_session)
    user = await user_repo.authenticate_user(username=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(subject=user.username)
    refresh_token = create_refresh_token(subject=user.username)

    response = {
        "access_token": access_token,  # must have as access_token to avoid errors with Swagger
        "refresh_token": refresh_token,
        "token_type": "Bearer",  # need this to avoid errors with Swagger
    }

    return jsonable_encoder(response)


@router.post("/jwt/refresh/", summary="Create new access token for user")
async def get_new_access_token_from_refresh_token(
    refresh_token_schema: RefreshTokenSchema,
    db_session: AsyncSession = Depends(get_async_session),
):
    user_repo = UserRepository(db_session)

    try:
        payload = jwt.decode(
            refresh_token_schema.refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ENCRYPTION_ALGORITHM],
        )
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Access Token")
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: User | None = await user_repo.get_user_by_username_or_email(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not active",
            headers={"WWW-Authenticate": "Bearer"},
        )

    new_access_token = create_access_token(
        username, expires_delta=timedelta(minutes=settings.NEW_ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    new_refresh_token = create_refresh_token(
        username, expires_delta=timedelta(settings.NEW_REFRESH_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": new_access_token, "refresh_token": new_refresh_token}
