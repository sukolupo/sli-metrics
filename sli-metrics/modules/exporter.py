from flask import request, Response
from prometheus_client import Counter, Histogram
import time
import sys
import os
import pathlib
import prometheus_client
from prometheus_client import multiprocess, CollectorRegistry

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

def process_metrics(metric_dir="../metrics", pattern=".metric"):
    directory = pathlib.Path(metric_dir)

    for f in directory.iterdir():
        if f.is_file() and f.name.endswith(pattern):
            m_name = f.name.split('.')[0]
            with open(os.path.join(directory,f.name),'r') as mfile:
                for line in mfile:
                    print(currentFile)

