# coding=utf-8
from celery import Celery

app = Celery('celery_demo')
app.config_from_object('celery_config')
