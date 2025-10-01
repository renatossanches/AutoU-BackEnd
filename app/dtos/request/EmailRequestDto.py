from pydantic import BaseModel, EmailStr

class EmailRequestDTO(BaseModel):
    receiver_email: EmailStr
    subject: str
    body: str
    
    model_config = {
        "from_attributes": True  
    }
