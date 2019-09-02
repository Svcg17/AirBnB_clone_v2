#!/usr/bin/python3
"""
The 3-python_route module
Starts a Flask web application
"""
from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Return: a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """
        Return: a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Return: a string followed by the value of the text variable
    """
    return ('C {}'.format(text).replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
        Return: a string followed by the value of the text variable
        with its default value as "is cool"
    """
    return ('Python {}'.format(text).replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
