from celery import Celery

from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


celery_app.conf.task_routes = {
    "app.tasks.email.send_welcome_email": {"queue": "emails"},
}
