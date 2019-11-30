#!/bin/python
from flask import Flask, Response
from modules.exporter import process_metrics

app = Flask(__name__)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

# setup_metrics(app)

@app.route('/')
def hello():
    return 'Hello from {0}'.format(app.name)

@app.route('/metrics', method = 'GET')
def collect_metrics():
    m = ""
    for i in process_metrics(app):
        m += i 

    r = Response(response=m, status=200, mimetype="application/xml")    
    r.headers["Content-Type"] = CONTENT_TYPE_LATEST
    return r

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

@app.route('/metrics', method = 'POST')
def write_metric():
    return 'Hello from {0}'.format(app.name)

def initdb():
    database = r'/app/sli-metrics/metrics/metrics.db"
  
    metric_table = """CREATE TABLE IF NOT EXISTS metric (
                                    name text NTO NULL,
                                    key_labels text NOT NULL,
                                    additional_labels text,
                                    description text,
                                    comment text,
                                    type text,
                                    value text NOT  NULL,
                                    ttl integer NOT NULL DEFAULT 0, 
                                    insert_date text NOT NULL,
                                    end_date text NOT NULL,
                                    PRIMARY KEY(name, key_labels)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create metrics table
        create_table(conn, metric_table)
    else:
        print("Error! cannot create the database connection.") 

if __name__ == '__main__':
    initdb()
    app.run()