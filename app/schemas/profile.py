from pydantic import BaseModel
from typing import Optional
import uuid

class ProfileCreate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    user_id: uuid.UUID
