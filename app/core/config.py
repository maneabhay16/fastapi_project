import os
from dotenv import load_dotenv


env_mode = os.getenv("ENV", "local")

load_dotenv(dotenv_path=f".env.{env_mode}")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
