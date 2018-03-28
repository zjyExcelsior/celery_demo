# coding=utf-8
from celery import Celery

app = Celery('celery_demo',
             broker='amqp://guest:guest@localhost:5672/celery_demo',
             backend='rpc://guest:guest@localhost:5672/celery_demo',
             include=['celery_demo.tasks'])

app.conf.update(
    result_expires=3600,
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['pickle']
)
