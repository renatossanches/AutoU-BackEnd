from sqlalchemy.orm import Session
from app.models.User import User

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, hashed_password: str, name: str):
    user = User(email=email, password=hashed_password, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
