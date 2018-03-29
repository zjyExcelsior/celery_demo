# celery_demo

启动 redis:

    $ docker run -d -p 6379:6379 --name redis redis:latest

启动 rabbitmq-server:

    $ docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:latest

创建 vhost:

    $ docker exec rabbitmq rabbitmqctl add_vhost celery_demo

创建 user:

    $ docker exec rabbitmq rabbitmqctl add_user testonly testonly

给创建的 user 赋予权限:

    # docker exec rabbitmq rabbitmqctl set_permissions -p celery_demo testonly ".*" ".*" ".*"

启动 celery worker:

    $ celery worker --app=celery_demo.celery_app --concurrency=4 --events --loglevel=info

启动 flower:

    $ flower --app=celery_demo.celery_app

测试：

    $ python test_tasks.py
