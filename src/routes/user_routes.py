from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session
from uuid import UUID
from src.database import get_db
from src.models.user_model import User
from src.services import user_service
from src.schemas.user_schema import UserBase, UserResponse, UserLogin


router = APIRouter(prefix="/api/user", tags=['users'])

@router.get("/", response_model=list[UserResponse])
def get_all_users(db : session = Depends(get_db)):
    users = user_service.get_all_users(db,User)
    return users

@router.post("/", response_model=UserResponse, status_code=201)
def insert_user(user : UserBase, db : session = Depends(get_db)):
    new_user = user_service.create_user(database=db, userData=user, userModel=User)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
def find_user_by_id(user_id : UUID,db : session = Depends(get_db)):
    user = user_service.get_user_by_id(database=db, userModel=User, user_id=user_id)
    if not user:
        raise HTTPException(404, "user not found")
    return user

# @router.put("/{user_id}", response_model=UserResponse)
# def update_user(user_data : UserBase, user_id : str, db : session = Depends(get_db)):
#     user = user_service.update_user(db, user_data, user_id, User)
#     if not user:
#         raise HTTPException(404, "user not found")
#     return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id : UUID,db : session = Depends(get_db)):
    result = user_service.delete_user(database=db, userModel=User, user_id=user_id)
    if result == 0:
        raise HTTPException(404, "user not found")
    return

@router.post("/login")
def user_login(userdata : UserLogin, db:session = Depends(get_db)):
    user = user_service.login_user(database=db, userModel=User, user=userdata)
    if not user:
        raise HTTPException(401,"please use correct creds")
    return user