from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.profile import Profile  # only for type hints

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    first_name: Optional[str]
    last_name: Optional[str]
    hashed_password: str

    # forward reference to Profile
    profile: Optional["Profile"] = Relationship(back_populates="user")
