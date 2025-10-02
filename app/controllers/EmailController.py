from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.EmailService import send_email, list_user_emails
from app.dtos.request.EmailRequestDto import EmailRequestDTO
from app.dtos.response.EmailResponseDto import EmailResponseDTO
from app.dtos.response.EmailResponseDtoWithSenderMail import EmailResponseDtoWithSenderMail
from app.utils.Security import get_current_user

router = APIRouter(prefix="/emails", tags=["emails"])

@router.post("/send", response_model=EmailResponseDTO)
def send_email_endpoint(email_request: EmailRequestDTO, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return send_email(db, email_request, current_user)


@router.get("/user/{user_id}", response_model=list[EmailResponseDtoWithSenderMail])
def list_emails(user_id: int, db: Session = Depends(get_db)):
    """
    Lista emails de um usuário
    """
    return list_user_emails(db, user_id)
