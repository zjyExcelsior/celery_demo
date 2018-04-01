# coding=utf-8
import celery
from celery.utils.log import get_task_logger

from celery_demo.celery_app import app
from celery_demo.model import Session, User

logger = get_task_logger(__name__)


class SQLAlchemyTask(celery.Task):
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('after_return....')
        Session.remove()
        super(SQLAlchemyTask, self).after_return(status, retval, task_id, args,
                                                 kwargs, einfo)


@app.task(base=SQLAlchemyTask)
def list_users():
    users = Session.query(User).limit(10).all()
    print('session id: {}'.format(id(Session())))  # 输出session id
    return users


@app.task(ignore_result=True)
def ignore_result_task():
    return 'ignore_result_task'


@app.task
def raise_exception_task():
    1 / 0


@app.task(bind=True)
def bounded_task(self, arg1, arg2, **kwargs):
    msg_fmt = 'Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'
    print(msg_fmt.format(self.request))
    return self.request.id


@app.task
def logger_task():
    logger.info('logger_task executing...')


@app.task(queue='web_tasks')
def task_route_by_queue():
    return 'route_by_queue...'


@app.task(routing_key='web.task_by_routing_key')
def task_route_by_routing_key():
    return 'route_by_routing_key...'


@app.task
def add(x, y):
    return x + y
