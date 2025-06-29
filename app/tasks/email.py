from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
import os

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME", "test@example.com"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", "123456"),
    MAIL_FROM=os.getenv("MAIL_FROM", "test@example.com"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 1025)),
    MAIL_SERVER=os.getenv("MAIL_SERVER", "mailpit"),
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=False,
    VALIDATE_CERTS=False
)

def send_real_email(email: EmailStr, name: str):
    message = MessageSchema(
        subject="Welcome!",
        recipients=[email],
        body=f"Hello {name}, welcome to our platform!",
        subtype="plain"
    )
    fm = FastMail(conf)
    print(f"📧 Sending welcome email to {email}...")
    # FIX: await the coroutine
    import asyncio
    asyncio.run(fm.send_message(message))
    print("✅ Email sent!")
