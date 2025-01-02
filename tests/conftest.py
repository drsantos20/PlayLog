import pytest
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from app.db.database import create_tables


@pytest.fixture(scope="function")
def db_session():
    DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
    
    session = Session(engine)
    
    create_tables()
    
    yield session
    
    SQLModel.metadata.drop_all(engine)
    session.close()
