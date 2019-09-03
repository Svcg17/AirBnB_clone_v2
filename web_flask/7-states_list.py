#!/usr/bin/python3
"""
The 7-states_list module
Starts a Flask web application
"""
from flask import Flask, escape, request, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext()
def storage_app(var=None):
    """ removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_hmtl():
    """ Displays an HTTML page
    """
    s = storage.all('States').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
