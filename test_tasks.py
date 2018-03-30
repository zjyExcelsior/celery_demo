# coding=utf-8
from celery_demo import tasks

if __name__ == '__main__':
    tasks.add.apply_async((3, 4))

    async_result = tasks.list_users.apply_async()
    while not async_result.ready():
        pass
    assert True == async_result.ready()
    print async_result.result

    async_result = tasks.ignore_result_task.apply_async()
    assert False == async_result.ready()
    assert None == async_result.result

    async_result = tasks.raise_exception_task.apply_async()
    while not async_result.ready():
        pass
    assert (True, True, False, 'FAILURE') == (async_result.ready(),
                                              async_result.failed(),
                                              async_result.successful(),
                                              async_result.state)
