# coding=utf-8
broker_url = 'amqp://testonly:testonly@localhost:5672/celery_demo'
result_backend = 'redis://localhost:6379/1'
include=['celery_demo.tasks']
result_expires=3600
task_serializer='msgpack'
result_serializer='pickle'
accept_content=['msgpack', 'pickle']