from app.tasks.celery_worker import celery_app

@celery_app.task
def send_welcome_email(email: str, name: str):
    print(f"📧 Sending welcome email to {email}...")
    # You can use `smtplib`, `fastapi-mail`, `sendgrid`, etc. to send email.
    print(f"Hello {name}, welcome to our platform!")
