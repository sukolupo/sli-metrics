#!/bin/python
from flask import Flask, Response
from modules.exporter import process_metrics

app = Flask(__name__)

# setup_metrics(app)

@app.route('/')
def hello():
    return 'Hello from {0}'.format(app.name)

@app.route('/metrics')
def collect_metrics():
    m = ""
    for i in process_metrics(app):
        m += i 

    r = Response(response=m, status=200, mimetype="application/xml")    
    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return m

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
    app.run()