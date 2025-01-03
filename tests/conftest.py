import asyncio
from contextlib import ExitStack

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from app.db.database import get_db, sessionmanager
from app.main import init_app


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield init_app(init_db=False)


@pytest.fixture
def client(app):
    with TestClient(app) as c:
        yield c


# @pytest.fixture(scope="session")
# def event_loop(request):
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()


# event_loop was removed from pytest 6.0.0 and it was used in connection_test fixture.
@pytest.fixture(scope="session", autouse=True)
async def connection_test():
    connection_str = "sqlite+aiosqlite:///:memory:"
    sessionmanager.init(connection_str)
    yield
    await sessionmanager.close()


@pytest.fixture(scope="function", autouse=True)
async def create_tables(connection_test):
    async with sessionmanager.connect() as connection:
        await sessionmanager.drop_all(connection)
        
         # This will create tables for all SQLModel models
        await connection.run_sync(SQLModel.metadata.create_all)


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, connection_test):
    async def get_db_override():
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_db_override
