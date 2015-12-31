#!/usr/bin/env python

from flask import jsonify, json
from sqlalchemy.sql import select
from app.dao.database import db_session
from app.models.userModel import UserModel



class UserController(object):
    _user = dict(name=None, email=None,
                 login=None, password=None,
                 role=0, avatar=None)
    
    def __init__(self, 
                 name=None, email=None,
                 login=None, password=None,
                 role=0, avatar=None):
        self.user = UserModel()
        
    
    def _getlistuser(self, *args, **kwargs):
        
        return listuser
    
    def adduser(self, ):
        db_session.add(self.user)
        db_session.commit()
        
    def get_all_users(self):
        # listofusers = db_session.query(UserModel).all()
        # print listofusers
        result = db_session.query(UserModel).all()
        listuser = list()
        user = dict()
        for key in result:
            user["name"] = key.name

            listuser.append(user)
        return json.dumps(listuser)
    
    
