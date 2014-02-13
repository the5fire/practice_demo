import subprocess
from time import sleep

from celery import Celery

backend = 'db+mysql://root:@localhost/celery'
broker = 'amqp://guest@localhost//'

app = Celery('tasks', backend=backend, broker=broker)


@app.task
def add(x, y):
    sleep(10)
    return x + y


@app.task
def hostname():
    return subprocess.check_output(['hostname'])
