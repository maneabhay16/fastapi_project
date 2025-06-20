from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.db import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
