#!/usr/bin/env python3

"""Import Modules"""

from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def basic_app():
    """Method that returns a JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """end-point to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Implement Login Route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
