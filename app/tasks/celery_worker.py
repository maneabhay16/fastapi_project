from celery import Celery
import os

broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
backend_url = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery("worker", broker=broker_url, backend=backend_url)

celery_app.conf.task_routes = {
    "app.tasks.email_tasks.send_welcome_email": {"queue": "emails"},
}

# Import to register the task
from app.tasks import email_tasks
