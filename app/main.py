from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.db.database import create_tables

app = FastAPI(title="FastAPI with SQLAlchemy")

# Include routes
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])


async def on_startup():
    create_tables()


app.add_event_handler("startup", on_startup)
