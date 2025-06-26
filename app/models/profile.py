from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from app.models.user import User

class Profile(SQLModel, table=True):
    __tablename__ = "profile"

    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: Optional[str] = None
    bio: Optional[str] = None

    user_id: uuid.UUID = Field(foreign_key="user.id", index=True, nullable=False)
    user: Optional["User"] = Relationship(back_populates="profile")
