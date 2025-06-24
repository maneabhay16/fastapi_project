from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.post("/")
def create_profile(profile_data: ProfileCreate, session: Session = Depends(get_session)):
    profile = Profile(**profile_data.dict())
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile
