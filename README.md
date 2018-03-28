# celery_demo

启动 celery worker:

    $ celery worker --app=celery_demo.celery_app --concurrency=4 --loglevel=info

启动 flower:

    $ flower --app=celery_demo.celery_app

测试：

    $ python test_tasks.py
