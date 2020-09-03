#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>')
def numplate(n):
    """
        Generate HTML code with a variable in it
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def oddeven(n):
    """
        Returns the type of the number Odd or Even
    """
    numbertype = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, numbertype=numbertype)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
