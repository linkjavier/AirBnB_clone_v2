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


@app.route('/c/<text>')
def return_last(text):
    """
        Display “C ” followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def return_python(text="is cool"):
    """
        Displays Python, followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def is_number(n):
    """
        Displays that if n is a number
    """
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
