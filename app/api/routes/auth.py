from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user import UserCreate, UserLogin
from app.core.security import verify_password, create_access_token
from app.crud.user import get_user_by_username, create_user
from app.db import engine
from app.tasks.email import send_welcome_email

from app.models.user import User
from typing import List
from sqlmodel import select
router = APIRouter()

def get_db():
    with Session(engine) as session:
        yield session

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = create_user(db, user)
    send_welcome_email.delay(user.email, user.first_name)
    return new_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}
