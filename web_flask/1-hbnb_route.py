#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def return_hello():
    """
        Function that returns Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def return_hbnb():
    """
        Function that returns HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
