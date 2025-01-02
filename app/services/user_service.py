from sqlmodel import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.db.database import engine


async def create_user(user: UserCreate):
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = user.password
    )
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    return new_user
