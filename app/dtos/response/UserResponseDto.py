from pydantic import BaseModel

class UserResponseDto(BaseModel):
    id: int
    email: str
    name: str

    model_config = {
        "from_attributes": True
    }
