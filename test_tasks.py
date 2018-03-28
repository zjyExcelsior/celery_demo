# coding=utf-8
from celery_demo import tasks

if __name__ == '__main__':
    tasks.add.apply_async((3, 4))

    async_result = tasks.list_users.apply_async()
    while not async_result.ready():
        pass
    print async_result.ready(), async_result.result
