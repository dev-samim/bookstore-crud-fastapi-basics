from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.env_config import DB_URL

if not DB_URL:
    raise RuntimeError("database_url is not set")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine,autoflush=False)


def get_db():
    db = SessionLocal()  
    try:
        yield db         
    finally:
        db.close()

Base = declarative_base()