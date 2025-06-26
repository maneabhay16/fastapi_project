# app/models/user.py
from sqlmodel import SQLModel, Field,Relationship
from app.models.profile import Profile
from typing import Optional
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    password: str
    # first_name: Optional[str] = None
    # last_name: Optional[str] = None
    email: Optional[str] = None
    profile: Optional["Profile"] = Relationship(back_populates="user")