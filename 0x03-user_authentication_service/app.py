#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_users() -> str:
    """Register user"""
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    else:
        return jsonify(
                {"email": "<registered email>", "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """Log in"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(401)

    user_login = AUTH.valid_login(email, password)
    if user_login is True:
        session_id = AUTH.create_session(email)
        res = jsonify({"email": "<user email>", "message": "logged in"})
        res.set_cookie("session_id", session_id)
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE', 'GET'], strict_slashes=False)
def logout():
    """Log out"""
    session_id = request.cookies.get("session_id", None)
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """User profile"""
    session_id = request.cookies.get("session_id", None)
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
