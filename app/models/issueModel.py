#!/usr/bin/env python

from sqlalchemy import Column, Integer, String

from app.dao.database import Base

class IssueModel(Base):
    
    """ This class is used for schema of Issue entity """
    
    __tablename__ = 'issue'

    id = Column('ID', Integer, primary_key=True)
    name = Column('NAME', String(60))
    description = Column('DESCRIPTION', String(256))
    map_pointer = Column('MAP_POINTER', String(128))
    priority = Column('PRIORITY_ID', Integer)
    status = Column('STATUS', String(20))
    category = Column('CATEGORY_ID', Integer)
    attacments = Column('ATTACHMENTS', String(256))
    
    def __init__(self,
                 name=None, description=None,
                 map_pointer="LatLng(0.00000, 0.00000)", priority=None,
                 status=None, category=0,
                 attacments=None):
        self.name = name
        self.description = description
        self.map_pointer = map_pointer
        self.priority = priority
        self.status = status
        self.category = category
        self.attacments = attacments
    