from app.tasks.email import send_real_email
from app.tasks.celery_worker import celery_app

@celery_app.task(name="app.tasks.email.send_welcome_email")
def send_welcome_email(email: str, name: str):
    print(f"📨 [TASK] About to send email to: {email}")
    try:
        send_real_email(email, name)
        print("✅ [TASK] Email successfully sent!")
    except Exception as e:
        print(f"❌ [TASK] Failed to send email: {e}")
