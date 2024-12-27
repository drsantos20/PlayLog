

from sqlmodel import Column, SQLModel, Integer, String


class User(SQLModel, table=True):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

