from src.database import Base
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID

class Book(Base):
    __tablename__ = "books"
    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    in_stock = Column(Boolean, default=True)
