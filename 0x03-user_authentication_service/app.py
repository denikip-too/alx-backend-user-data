#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask
from flask import jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", method=['GET'], strict_slashes=False)
def index() -> str:
    """return a JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("users", method=['POST'], strict_slashes=False)
def users(email: str, password: str) -> str:
    """Register user"""
    try:
        user = AUTH.register_user(email, password)
    except NoResultFound:
        user = AUTH._db.add_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    else:
        abort(400)
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
