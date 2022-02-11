from pydantic import BaseModel
from typing import Optional

from app.database import Base

# Creating a schema, for checking if the user provided the apporpriate fields
class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True

class PostCreate(PostBase):
    pass