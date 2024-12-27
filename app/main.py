from fastapi import FastAPI
from app.api.v1.endpoints import user

app = FastAPI(title="FastAPI with SQLAlchemy")

# Include routes
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
