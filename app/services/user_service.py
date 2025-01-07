from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select

from app.db.models.user import User
from app.schemas.user import UserCreate


async def create_user(user: UserCreate, db: AsyncSession):
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = user.password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user(username: str, db: AsyncSession):
    find_user = await db.execute(
        select(User).where(User.username == username)
    )
    fetched_user = find_user.scalars().first()
    return fetched_user
