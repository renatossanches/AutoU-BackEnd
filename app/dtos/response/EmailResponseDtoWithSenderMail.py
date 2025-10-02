from pydantic import BaseModel

class EmailResponseDtoWithSenderMail(BaseModel):
    id: int
    sender_id: int
    sender_email: str
    receiver_id: int
    receiver_email: str
    subject: str
    body: str
    categoria: str
    is_important: bool

    model_config = {
        "from_attributes": True  
    }
