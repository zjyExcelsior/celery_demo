# coding=utf-8
import celery

from celery_demo.celery_app import app
from celery_demo.model import Session, User


class SQLAlchemyTask(celery.Task):
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('after_return....')
        Session.remove()


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
    1/0


@app.task
def add(x, y):
    return x + y
