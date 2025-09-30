from sqlalchemy.orm import Session
from app.models.Email import Email

def create_email(db: Session, sender_id: int, receiver_id: int, subject: str, body: str, is_important: bool, categoria: str):
    email = Email(
        sender_id=sender_id,
        receiver_id=receiver_id,
        subject=subject,
        body=body,
        is_important=is_important,
        categoria=categoria
    )
    db.add(email)
    db.commit()
    db.refresh(email)
    return email

def get_emails_by_user(db: Session, user_id: int):
    return db.query(Email).filter(Email.receiver_id == user_id).all()
