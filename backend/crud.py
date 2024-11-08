import pyotp
import bcrypt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from database import sessionLocal

def generate_otp():
    otp = pyotp.TOTP("base32secret3232").now()
    return otp

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def generate_user_otp(db: Session, email: str):
    user = get_user_by_email(db, email)
    if user:
        otp = generate_otp()
        user.otp = otp
        user.otp_expiry = datetime.now() + timedelta(minutes = 5)
        db.commit()
        db.refresh(user)
        return otp
    return None

def verify_user_otp(db: Session, email: str, otp: str):
    user = get_user_by_email(db, email)
    if user and user.otp == otp:
        if user.otp_expiry > datetime.now():
            return True
        return False