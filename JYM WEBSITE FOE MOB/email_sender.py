
import smtplib
import secrets


from email.message import EmailMessage

def generate_otp():

    otp = str(secrets.randbelow(900000) + 100000)

    return otp

otp = generate_otp()

print(otp)

def send_email(receiver_email, otp):

    sender_email = "rinkusingh8126099319@gmail.com"
    app_password = "zyxwmisnvnuogwvi"

    message = EmailMessage()

    message["Subject"] = "RJ Projects - Email Verification"
    message["From"] = sender_email
    message["To"] = receiver_email

    message.set_content(
        f"Your OTP for email verification is: {otp}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(sender_email, app_password)

        server.send_message(message)

    return True

receiver_email = "rinkusingh8126099319@gmail.com"

send_email(receiver_email, otp)

print("EMAIL SENT SUCCESSFULLY!")
