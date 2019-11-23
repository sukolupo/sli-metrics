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
    #process_metrics()
    return process_metrics()

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
    app.run()