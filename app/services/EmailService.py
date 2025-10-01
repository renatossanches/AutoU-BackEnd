from sqlalchemy.orm import Session
from app.repositories.EmailRepository import create_email, get_emails_by_user
from app.repositories.UserRepository import get_user_by_email
from app.ai.EmailClassifier import predict_importance
from app.dtos.request.EmailRequestDto import EmailRequestDTO
from app.dtos.response.EmailResponseDto import EmailResponseDTO

def send_email(db: Session, sender_id: int, email_request: EmailRequestDTO) -> EmailResponseDTO:
    # Buscar usuário destinatário
    receiver = get_user_by_email(db, email_request.receiver_email)
    if not receiver:
        raise Exception("Destinatário não encontrado")

    # Classificação com IA - deve retornar boolean
    is_important = bool(predict_importance(email_request.subject, email_request.body))
    
    # Categoria textual
    categoria = "Produtivo" if is_important else "Improdutivo"

    # Criar email no banco
    email = create_email(
        db=db,
        sender_id=sender_id,
        receiver_id=receiver.id,
        subject=email_request.subject,
        body=email_request.body,
        is_important=is_important,
        categoria=categoria
    )

    # Retorno estruturado
    return EmailResponseDTO(
        id=email.id,
        sender_id=email.sender_id,
        receiver_id=email.receiver_id,
        subject=email.subject,
        body=email.body,
        categoria=categoria,
        is_important=is_important
    )


def list_user_emails(db: Session, user_id: int):
    emails = get_emails_by_user(db, user_id)
    response = []
    for e in emails:
        response.append(EmailResponseDTO(
            id=e.id,
            sender_id=e.sender_id,
            receiver_id=e.receiver_id,
            subject=e.subject,
            body=e.body,
            categoria=e.categoria,
            is_important=bool(e.is_important)  
        ))
    return response
