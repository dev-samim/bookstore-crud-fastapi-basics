from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class bookBase(BaseModel):
    name : str
    author : str
    price : int 
    in_stock : Optional[bool] = None


class bookUpdate(BaseModel):
    name : Optional[str] = None
    author : Optional[str] = None
    price : Optional[int] = None
    in_stock : Optional[bool] = None
    
class bookResponse(bookBase):
    id : UUID
    class Config:
        from_attributes = True
        