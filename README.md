# celery_demo

启动 rabbitmq-server 和 redis:

    $ docker-compose up -d

在 rabbitmq-server 中创建 vhost, user, 并给 user 赋予权限:

    $ ./init_rabbitmq.sh

启动 celery worker(消费者):

    $ celery multi start celery_demo1 celery_demo2 --app=celery_demo --concurrency=4 --events --loglevel=info --pidfile=/tmp/%n.pid --logfile=/tmp/%n%I.log --statedb=/tmp/%n.state --autoscale=4,2

重启 celery worker(消费者):

    celery multi restart celery_demo1 celery_demo2 --pidfile=/tmp/%n.pid

停止 celery worker(消费者):

    $ celery multi stop celery_demo1 celery_demo2 --pidfile=/tmp/%n.pid

启动 flower:

    $ flower --app=celery_demo.celery_app

测试：

    $ python test_tasks.py
