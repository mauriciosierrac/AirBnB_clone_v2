#!/usr/bin/python3
''' this app run the serve and print hello HBNH'''

from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    ''' print a hello page '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
