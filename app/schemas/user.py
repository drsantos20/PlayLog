from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

    
class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

    