from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    name: str 
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: UUID
    name: str 
    email: EmailStr
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponse(BaseModel):
    id: UUID
    name: str 
    email: EmailStr
    access_token: str
    class Config:
        from_attributes = True
    class ConfigDict:
        exclude = {'created_at', 'updated_at'}
    
# class UserUpdate:
#     name: Optional[str] = None
#     email: Optional[EmailStr] = None
#     password: Optional[str] = None
