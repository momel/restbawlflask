#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Table, MetaData

from app.dao.database import Base, engine

class UserModel(Base):
    
    """ """
    metadata = MetaData()
    __tablename__ = 'users'
    id = Column("ID", Integer, primary_key=True)
    name = Column("NAME", String(50), unique=True)
    email = Column("EMAIL", String(80), unique=True)
    login = Column("LOGIN", String(40), unique=True)
    password = Column("PASSWROD", String(128))
    role = Column("ROLE_ID", Integer)
    avatar = Column("AVATAR_URL", String(256))
    """  
    def __init__(self,
                 name=None, email=None,
                 login=None, password=None,
                 role=0, avatar=None):
        self.name = name
        self.email = email
        self.login = login
        self.password = password
        self.role = role
        self.avatar = avatar
        
    def __getattr__(self,):
        newdict = dict(
            name = self.name,
            email = self.email
        )
        
    """     
