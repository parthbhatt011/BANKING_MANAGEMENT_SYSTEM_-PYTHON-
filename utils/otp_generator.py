import pyotp

secret = pyotp.random_base32()

totp = pyotp.TOTP(secret, interval=300)   # OTP valid for 5 minutes

otp = totp.now()

return otp;