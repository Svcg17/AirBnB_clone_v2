#!/usr/bin/python3
"""
The 10-hbnb_filters module
Starts a Flask web application
"""
from flask import Flask, escape, request, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_and_amenities():
    """ Displays an HTTML page
    """
    return render_template('10-hbnb_filters.html',
                           i=storage.all(State).values(),
                           j=storage.all(Amenity).values())


@app.teardown_appcontext
def storage_app(var=None):
    """ removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
