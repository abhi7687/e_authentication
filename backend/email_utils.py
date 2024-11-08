import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

def generate_otp(length=6):
    """Generates a random OTP with digits."""
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

def send_otp_email(user_email, otp):
    """Sends the OTP to the user's email."""
    sender_email = "abhiramvaitla8@gmail.com"  # Replace with your email
    sender_password = "@123456789Bhi"  # Replace with your email password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = 'Your OTP Code'

    body = f"Your OTP code is {otp}."
    message.attach(MIMEText(body, 'plain'))

    # Establish connection to Gmail SMTP server and send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, user_email, text)
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Failed to send OTP: {e}")
