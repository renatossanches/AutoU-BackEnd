from sqlalchemy.orm import Session
from app.repositories.UserRepository import get_user_by_email, create_user
from app.utils.Security import hash_password, verify_password, create_access_token
from app.dtos.response import UserResponse, LoginResponse
def register_user(db: Session, email: str, password: str, name: str):
    if get_user_by_email(db, email):
        raise Exception("User already exists")
    hashed = hash_password(password)
    return create_user(db, email, hashed, name)

def login_user(db: Session, email: str, password: str) -> UserResponse:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise Exception("Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    
    # Retorna dados do usuário + token
    return LoginResponse(id=user.id, email=user.email, name=user.name, access_token=token)
