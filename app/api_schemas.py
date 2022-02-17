from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

from app.database import Base

# Creating a schema, for checking if the user provided the apporpriate fields
class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config: 
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str