from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user

router = APIRouter()

@router.post("/create", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_data = await create_user(user, db)
    return user_data


@router.get("/user", response_model=UserResponse)
async def get_user_by_username(username: str, db: AsyncSession = Depends(get_db)):
    user = await get_user(username, db)
    return user
