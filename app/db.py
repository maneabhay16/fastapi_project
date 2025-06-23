import os
from sqlmodel import SQLModel, create_engine
from app.core.config import DATABASE_URL 

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
