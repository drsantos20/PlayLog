from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr

    
class UserCreate(UserBase):
    password: str
    

class UserUpdate(BaseModel):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    email: str
    
    model_config = ConfigDict(str_max_length=50)
