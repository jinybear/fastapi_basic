from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models import Base, SessionLocal

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)

