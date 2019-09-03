#!/usr/bin/python3
"""
The 8-cities_by_states module
Starts a Flask web application
"""
from flask import Flask, escape, request, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays an HTTML page
    """
    return render_template('8-cities_by_states.html',
                           i=storage.all('State').values(),
                           j=storage.all('City').values())


@app.teardown_appcontext
def storage_app(var=None):
    """ removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)