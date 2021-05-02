#!/usr/bin/python3
''' first app with 2 routes'''

from flask import Flask, escape, render_template


app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''return index page'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def page():
    '''return another page'''
    return 'HBNB'


@app.route('/c/<text>')
def pagec(text):
    ''' capture a argument and print in page'''
    str = 'C {}'.format(escape(text))
    return str.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def page_python(text='is cool'):
    ''' capture a argument and print in page'''
    str = 'Python {}'.format(text)
    return str.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    ''' capture a argument and print in page'''
    if type(n) == int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    ''' capture a argument and print in page'''
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd(n):
    ''' capture a argument and print in page'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
