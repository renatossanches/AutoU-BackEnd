from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.UserService import register_user, login_user
from app.dtos.request.UserRequestDto import UserCreate, UserLogin
from app.dtos.response.UserResponseDto import UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user.email, user.password, user.name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user(db, user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
