#!/usr/bin/python3
"""
The 7-states_list module
Starts a Flask web application
"""
from flask import Flask, escape, requesti, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext()
def storage_app():
    """ removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_hmtl():
    """ Displays an HTTML page
    """
    s = storage.all('States')
    return(s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
