from sqlmodel import Session, select
from app.models.user import User
from app.core.security import hash_password

def get_user_by_username(db: Session, username: str):
    return db.exec(select(User).where(User.username == username)).first()

def create_user(db: Session, username: str, password: str):
    user = User(username=username, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
