from celery import Celery
import os

broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")

celery_app = Celery("worker", broker=broker_url, backend=broker_url)

celery_app.conf.task_acks_late = True           
celery_app.conf.worker_prefetch_multiplier = 1 
celery_app.conf.task_routes = {
    "app.tasks.email.send_welcome_email": {"queue": "emails"},
}
