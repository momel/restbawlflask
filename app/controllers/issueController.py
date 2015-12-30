#!/usr/bin/env python

from app.models import IssueModel

class IssueController(object):
    
    def __init__(self, ):
        self.issue = IssueModel()
