#!/usr/bin/env python

from flask import (
    url_for,
    session,
    Response,
    jsonify,
)

from app import app

@app.route("/", methods=["GET"])
def index():
    return Response({"Message": "Have a nice day! :)"}, 200)


@app.route("/users/all", methods=["GET"])
def get_all_ussers():
    """ This method return list of dictionary by all users
        in the system.
        Method return data in JSON format.
        
        Example:
        [{"usermane": "ahardy", "id": "3", "role": "ADMIN", "fullname": "Arnold Hardy"},
         {"usermane": "hgudin", "id": "1", "role": "MANAGER", "fullname": "Garry Gudini"},]
    """
    pass


@app.route("/users/current", methods=["GET"])
def get_current_user():
    """ This method return dictionary of current loginned
        users in the system.
        Method return data in JSON format.
        
        Example:
        {"usermane": "ahardy", "id": "3", "role": "ADMIN", "fullname": "Arnold Hardy"}
    """
    pass


@app.route("/users/auth/login", methods=["POST"])
def user_login():
    pass

@app.route("/users/auth/logout", methods=["GET"])
def logout():
    pass


@app.route("/users", methods=["POST"])
def add_new_user():
    pass


@app.route("/users/<int:id>", methods=["PUT"])
def edit_user():
    pass


@app.route("/users/validate", methods=["POST"])
def email_confirmation():
    pass


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user():
    pass


@app.route("/users/changepass", methods=["GET"])
def reset_user_password():
    pass
