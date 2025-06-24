from pydantic import BaseModel
from typing import Optional

class ProfileCreate(BaseModel):
    full_name: Optional[str]
    bio: Optional[str]
    user_id: int
