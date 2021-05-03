#!/usr/bin/python3
'''list states web page'''

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)

app.url_map.stric_slashes = False


@app.route('/states_list')
def states_list():
    '''this method show a web page with list
    of content with states'''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    '''close the sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
