#!/usr/bin/python3
'''list states web page'''

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)

app.url_map.stric_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    '''this method show a web page with list
    of content with states'''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    '''close the sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
