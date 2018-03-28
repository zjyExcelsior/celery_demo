# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session

connect_params = {
    'dialect': 'mysql',
    'driver': 'pymysql',
    'username': 'testonly',
    'password': 'testonly',
    'host': 'localhost',
    'port': 3306,
    'database': 'comment_demo'
}
DB_URI = ('{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'
          '?charset=utf8').format(**connect_params)

engine = create_engine(DB_URI, echo=False)
Base = declarative_base()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


def create_tables(engine):
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), doc='my name')
    password = Column(String(20), doc='my password')

    def __repr__(self):
        return '<User(name="%s", password="%s")>' % (self.name, self.password)


if __name__ == '__main__':
    drop_tables(engine)
    create_tables(engine)
