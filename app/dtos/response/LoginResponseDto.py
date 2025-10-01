from pydantic import BaseModel

class LoginResponse(BaseModel):
    id: int
    email: str
    name: str
    access_token: str

    model_config = {
        "from_attributes": True
    }
