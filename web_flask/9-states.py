#!/usr/bin/python3
"""
The 9-states module
Starts a Flask web application
"""
from flask import Flask, escape, request, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def cities_by_states():
    """ Displays an HTTML page
    """
    return render_template('9-states.html',
                           i=storage.all('State').values())


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states_by_id(id):
    """
    Displays an HTML page
    """
    return render_template('9-states.html',
                           j=storage.all('State').values(), id=id)


@app.teardown_appcontext
def storage_app(var=None):
    """ removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
