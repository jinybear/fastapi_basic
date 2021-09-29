from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models

class User(models.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    full_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    

