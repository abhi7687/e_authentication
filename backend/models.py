from sqlalchemy import Column, Integer, String, DateTime # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    otp = Column(String)
    otp_expiry = Column(DateTime)