from pydantic import BaseModel

class EmailResponseDTO(BaseModel):
    id: int
    sender_id: int
    sender_email: str
    receiver_id: int
    subject: str
    body: str
    categoria: str
    is_important: bool

    model_config = {
        "from_attributes": True  
    }
