#!/usr/bin/env python

from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE = 'sqlite://///Users/user/Documents/Projects/bawlPython/bawl.db'
DEBUG = True
SECRET_KEY = 'hj3lwe92g489hfsk'
USERNAME = 'admin'
PASSWORD = 'Install_new!'

engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
