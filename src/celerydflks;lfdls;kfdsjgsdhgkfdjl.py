from celery import Celery

app = Celery('src', broker='redis://localhost:6379/0')

app.conf.update(
    result_backend='redis://localhost:6379/0',
    imports=['src.tasks']
)
