from app.tasks.celery_worker import celery_app

@celery_app.task(bind=True, max_retries=3, default_retry_delay=10)
def send_welcome_email(self, email: str, name: str):
    try:
        print(f"📧 Sending welcome email to {email}...")
        print(f"Hello {name}, welcome to our platform!")
        # send_email_function(email, name)
    except Exception as exc:
        raise self.retry(exc=exc)
