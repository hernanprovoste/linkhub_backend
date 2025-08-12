from fastapi import APIRouter
from app.core.models import User, UserCreate
from datetime import datetime

router = APIRouter()

@router.post("/users/", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    user_dict = user.model_dump()
    return User(
        id=1,
        created_at=datetime.now(),
        **user_dict
    )