from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    username: str
    email:EmailStr
    # first_name:str
    # last_name:str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
