from sqlmodel import SQLModel, create_engine, Session
from app.models.profile import Profile
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session