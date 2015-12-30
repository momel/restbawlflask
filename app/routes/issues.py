#!/usr/bin/env python

from flask import (
    url_for,
    session,
    Response,
    jsonify,
)

from app import app

@app.route("/issue/all", methods=["GET"])
def get_all_issues():
    return "Issues"


@app.route("/issue/<int:id>", methods=["GET"])
def get_issue_by_id():
    pass


@app.route("/issue/<int:id>/history", methods=["GET"])
def get_issue_history_by_issue_id():
    pass


@app.route("/issue/<int:id>/delete", methods=["DELETE"])
def delete_issue():
    pass


@app.route("/issue/resolved", methods=["GET"])
def get_resolved_issue():
    pass


@app.route("/issue", methods=["POST"])
def add_issue():
    pass


@app.route("/issue/<int:id>", methods=["PUT"])
def edit_issue():
    pass


@app.route("/issue/<int:id>/resolve", methods=["PUT"])
def to_resolve_issue():
    pass
