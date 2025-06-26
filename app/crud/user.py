from sqlmodel import Session, select
from app.models.user import User
from app.core.security import hash_password
from app.schemas.user import UserCreate

def get_user_by_username(db: Session, username: str):
    return db.exec(select(User).where(User.username == username)).first()

def create_user(db: Session, user_data: UserCreate):
    user = User(
        username=user_data.username,
        email=user_data.email,
        # first_name=user_data.first_name,
        # last_name=user_data.last_name,
        password=hash_password(user_data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

