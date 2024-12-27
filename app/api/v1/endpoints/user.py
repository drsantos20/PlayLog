from fastapi import APIRouter, Depends, HTTPException

from app.schemas.user import UserCreate, UserResponse


router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate):
    # TODO: Create a new user in the database using the service layer
    return {"name": user.name, "email": user.email, "password": user.password, "id": 1, "is_active": True}
