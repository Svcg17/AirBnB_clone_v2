#!/usr/bin/python3
"""
The 2-c_route module
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
        Returns: a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Returns: a string followed by the value of the text variable
    """
    return ('C {}'.format(text).replace("_", " "))


app.run(host='0.0.0.0', port=5000)