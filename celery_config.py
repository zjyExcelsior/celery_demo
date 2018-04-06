# coding=utf-8
from kombu import Exchange, Queue

broker_url = 'amqp://testonly:testonly@localhost:5672/celery_demo'
# redis_host, redis_port, redis_db, redis_password 用于 RedisBackend
redis_host = 'localhost'
redis_port = 6379
redis_db = 1
# redis_password =
result_backend = 'redis://localhost:6379/1'
include = ['celery_demo.tasks']
result_expires = 3600 * 24
task_serializer = 'msgpack'
result_serializer = 'json'
accept_content = ['msgpack', 'json', 'pickle']

default_exchange = Exchange('default', type='topic')
task_queues = (  # 定义任务队列(routing_key表示binding key)
    Queue('default', default_exchange, routing_key='task.#'),
    Queue('web_tasks', default_exchange, routing_key='web.#')
)
task_default_queue = 'default'
task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.default'

task_routes = {
    'celery_demo.tasks.list_users': {
        'queue': 'web_tasks',
        'routing_key': 'web.list_users'
    }
}
