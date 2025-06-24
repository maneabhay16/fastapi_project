from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User  # only for type hints

class Profile(SQLModel, table=True):
    __tablename__ = "profile"
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: Optional[str]
    bio: Optional[str]

    user_id: int = Field(foreign_key="user.id", index=True, nullable=False)

    user: Optional["User"] = Relationship(back_populates="profile")
