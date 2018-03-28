# coding=utf-8
import celery

from celery_demo.celery_app import app
from celery_demo.model import Session, User


class SQLAlchemyTask(celery.Task):
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('after_return....')
        Session.remove()


@app.task
def add(x, y):
    return x + y


@app.task(base=SQLAlchemyTask)
def list_users():
    users = Session.query(User).limit(10).all()
    print('session id: {}'.format(id(Session())))  # 输出session id
    return users
