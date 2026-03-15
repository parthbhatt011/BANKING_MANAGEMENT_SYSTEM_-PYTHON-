import random
from datetime import datetime
import pyotp
import smtplib

def generate_userid():
    return random.randint(10000000, 99999999)

def generate_account_number():
    return random.randint(10000000, 99999999)

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_transaction_description(transaction_type, amount):
    return f"{transaction_type.capitalize()} of {amount}"

def otp_generater():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret, interval=300)   # 5 minutes
    otp = totp.now()
    return otp, totp

def otp_sender(email,otp):
    sender = "your_email@gmail.com"
    password = "app_password"
    message = f"""Subject: OTP Verification For Banking Management System

    Your OTP is: {otp}
    It will expire in 5 minutes.
"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, email, message)
    server.quit()

def otp_verifier(totp):
    user_otp = input("Enter OTP: ")
    if totp.verify(user_otp):
        print("OTP verified successfully")
        return True
    else:
        print("Invalid or expired OTP")
        return False