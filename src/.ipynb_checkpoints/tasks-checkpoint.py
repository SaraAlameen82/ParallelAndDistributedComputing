from celery import Celery

app = Celery('tasks', broker ='pyamqp://guest@localhost//', backend='redis://localhost:6380/0')

@app.task
def power(number, power):
    return number ** power

