from urllib import request
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import session
from uuid import UUID
from src.database import get_db
from src.dependencies.auth import verify_authentication
from src.models.user_model import User
from src.services import user_service
from src.schemas.user_schema import UserBase, UserResponse, UserLogin, UserLoginResponse


router = APIRouter(prefix="/api/user", tags=['users'])

@router.get("/", response_model=list[UserResponse])
def get_all_users(db : session = Depends(get_db)):
    users = user_service.get_all_users(db,User)
    return users

@router.post("/", response_model=UserResponse, status_code=201)
def insert_user(user : UserBase, db : session = Depends(get_db)):
    new_user = user_service.create_user(database=db, userData=user, userModel=User)
    return new_user

@router.get("/me", response_model=UserResponse)
def get_current_user(request: Request, db:session = Depends(get_db), user_id: str = Depends(verify_authentication)):
    user = user_service.get_current_user(database=db, request=request, user_id=user_id)
    if not user:
        raise HTTPException(404, "user not found")
    return user   

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

@router.post("/login", response_model=UserLoginResponse)
def user_login(userdata : UserLogin,response: Response, db:session = Depends(get_db)):
    user, access_token = user_service.login_user(database=db, userModel=User, user=userdata)
    print(user, access_token)
    if not user:
        raise HTTPException(401,"please use correct creds")
    response.set_cookie("access_token", access_token, httponly=True)
    return {"id": user.id, "name": user.name, "email": user.email, "access_token": access_token}
