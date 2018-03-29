# coding=utf-8
from celery import Celery

app = Celery('celery_demo',
             broker='amqp://testonly:testonly@localhost:5672/celery_demo',
             backend='redis://localhost:6379/1',
             include=['celery_demo.tasks'])

app.conf.update(
    result_expires=3600,
    task_serializer='msgpack',
    result_serializer='pickle',
    accept_content=['msgpack', 'pickle']
)
