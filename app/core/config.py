import os
from dotenv import load_dotenv

load_dotenv()
# check for postgress and setup pariksha and prepstudy so that can plugin 
# add testing locust
#write test cases 
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
