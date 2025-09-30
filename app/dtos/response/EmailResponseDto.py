from pydantic import BaseModel

class EmailResponseDTO(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    subject: str
    body: str
    categoria: str
    is_important: bool

    class Config:
        orm_mode = True
