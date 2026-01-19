import jwt
from fastapi import HTTPException, Request
from src.config.env_config import JWT_SECRET_KEY
from src.core.security import decode_jwt_token


def verify_authentication(request: Request) -> str :
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(401, "Access token not found")
    try:
        payload = decode_jwt_token(token, JWT_SECRET_KEY)
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(401, "Invalid token")
        return user_id
        
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid token")



    
    