from typing import Optional
from pydantic import BaseModel

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
    id : int
    class Config:
        orm_mode = True