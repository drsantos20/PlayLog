from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user


router = APIRouter()

@router.post("/create", response_model=UserResponse)
async def create_new_user(user: UserCreate):
    user_data = await create_user(user)
    return user_data
