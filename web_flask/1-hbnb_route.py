#!/usr/bin/python3
""" import flask """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ hello function content """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnh content"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000
