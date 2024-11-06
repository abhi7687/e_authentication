from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session # type: ignore
import crud
import models
import schemas
import database
import email_utils

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user or not crud.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    otp = crud.generate_user_otp(db, email=user.email)
    if not otp:
        raise HTTPException(status_code=400, detail="OTP generation failed")
    return {"message": "OTP sent to your email", "otp": otp}

@app.post("/send-otp/")
async def send_otp_to_email(user_email: str, db: Session = Depends(database.get_db)):
    otp = email_utils.generate_otp()  # Generate OTP
    email_utils.send_otp_email(user_email, otp)  # Send OTP to the provided email
    # Store OTP in the database or session (optional)
    return {"message": "OTP sent to your email!"}

@app.post("/verify_otp")
def verify_otp(otp: schemas.OTP, db: Session = Depends(database.get_db)):
    is_verified = crud.verify_user_otp(db, email=otp_data.email, otp=otp_data.otp)
    if not is_verified:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    return {"message": "OTP verified successfully, authentication completed."}
