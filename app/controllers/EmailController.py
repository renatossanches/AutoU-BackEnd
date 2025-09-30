from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.EmailService import send_email, list_user_emails
from app.dtos.request.EmailRequestDto import EmailRequestDTO
from app.dtos.response.EmailResponseDto import EmailResponseDTO

router = APIRouter(prefix="/emails", tags=["emails"])

@router.post("/send", response_model=EmailResponseDTO)
def send(email_request: EmailRequestDTO, db: Session = Depends(get_db), sender_id: int = 1):
    """
    Envia um email e classifica usando IA.
    sender_id por enquanto é fixo, futuramente pode vir do JWT.
    """
    try:
        return send_email(db, sender_id, email_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}", response_model=list[EmailResponseDTO])
def list_emails(user_id: int, db: Session = Depends(get_db)):
    """
    Lista emails de um usuário
    """
    return list_user_emails(db, user_id)
