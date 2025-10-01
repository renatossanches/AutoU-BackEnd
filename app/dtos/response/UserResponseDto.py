from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

    model_config = {
        "from_attributes": True
    }
