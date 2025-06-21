from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    # add first name and last name fields then create a fk realtionship and put migration aremove migration and check restore
    # celebry for email steup 
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email:str =Field(unique=True, index=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    hashed_password: str
