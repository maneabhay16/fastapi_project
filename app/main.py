from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.api.routes import profile
from app.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
