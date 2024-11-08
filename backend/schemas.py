from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class OTP(BaseModel):
    email: str
    otp: str