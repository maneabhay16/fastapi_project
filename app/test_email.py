import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

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
        subject="Test Email",
        recipients=[email],
        body=f"Hello {name}, this is a test email directly without Celery.",
        subtype="plain"
    )
    fm = FastMail(conf)
    fm.send_message(message)

# Test function
if __name__ == "__main__":
    send_real_email("test@example.com", "Chaitali")
    print("✅ Test email sent directly!")
