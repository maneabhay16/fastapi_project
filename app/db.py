import os
from sqlmodel import SQLModel, create_engine, Session
from app.models.profile import Profile

# from app.db_engine import engine  # Removed unresolved import; using local engine below




from app.core.config import DATABASE_URL

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    pass
    # SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session