from enum import Enum
from pydantic import BaseModel

class Genre(str, Enum):
    rock = "Rock"
    grunge = "Grunge"
    alternative = "Alternative"
    progressive_rock = "Progressive Rock"   

class Band(BaseModel):
    id: int
    name: str
    genre: str