from celery import Celery

app = Celery('tasks', broker ='pyamqp://guest@localhost//')

@app.task
def power(number, power):
    return number ** power

