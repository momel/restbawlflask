# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask

from app.dao import database

app = Flask(__name__)
app.Debug = True

from app.routes import (
    users,
    issues
)

from app.models import (
    userModel,
    issueModel
)

database.init_db()
