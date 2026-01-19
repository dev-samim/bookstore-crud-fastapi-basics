from passlib.context import CryptContext
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict, secret_key: str, algorithm: str = "HS256") -> str:
    """Create a JWT access token."""
    return jwt.encode(data, secret_key, algorithm=algorithm)

def decode_jwt_token(token: str, secret_key: str, algorithms: list = ["HS256"]) -> dict:
    """Decode a JWT access token."""
    return jwt.decode(token, secret_key, algorithms=algorithms)