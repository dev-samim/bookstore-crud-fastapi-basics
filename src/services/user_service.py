from fastapi import Request
from sqlalchemy.orm import session
from uuid import UUID
from src.schemas.user_schema import UserBase, UserResponse, UserLogin
from src.models.user_model import User
from src.core.security import hash_password, verify_password, create_jwt_token
from src.config.env_config import JWT_SECRET_KEY
from src.dependencies.auth import verify_authentication

def create_user(database : session, userModel : User, userData : UserBase) -> User:
    new_user = userModel(name=userData.name, email=userData.email, password=hash_password(userData.password))
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user

def get_user_by_email(database : session, userModel : User, email : str) -> User:
    return database.query(userModel).filter(userModel.email == email).first()

def get_user_by_id(database : session, userModel : User, user_id : UUID) -> User:
    return database.query(userModel).filter(userModel.id == user_id).first()

def get_all_users(database : session, userModel : User) -> list[User]:
    return database.query(userModel).all()

def delete_user(database : session, userModel : User, user_id : UUID) -> None:
    user_to_delete = database.query(userModel).filter(userModel.id == user_id).first()
    if user_to_delete:
        database.delete(user_to_delete)
        database.commit()
    return None 

def update_user(database : session, userModel : User, user_id : UUID, userData : User) -> User:
    user_to_update = database.query(userModel).filter(userModel.id == user_id).first()
    if user_to_update:
        user_to_update.name = userData.name
        user_to_update.email = userData.email
        user_to_update.password = hash_password(userData.password)
        database.commit()
        database.refresh(user_to_update)
    return user_to_update

def login_user(database : session, userModel : User, user : UserLogin):
    user_to_login : User | None = database.query(userModel).filter(userModel.email == user.email).first()
    if user_to_login and verify_password(user.password, user_to_login.password):
        access_token = create_jwt_token(data={"user_id" : str(user_to_login.id)}, secret_key=JWT_SECRET_KEY)
        return user_to_login, access_token
    return None

def get_current_user(database : session, request: Request, user_id: str) -> User:
    return database.query(User).filter(User.id == user_id).first()