from flask import request, Response
from prometheus_client import Counter, Histogram
import time
import sys
import prometheus_client
from prometheus_client import multiprocess, CollectorRegistry

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')