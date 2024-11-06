from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

class OTPVerify(BaseModel):
    email: str
    otp: str