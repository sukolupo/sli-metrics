from flask import request, Response
from prometheus_client import Counter, Histogram
import time
import sys
import os
import pathlib
import prometheus_client
from prometheus_client import multiprocess, CollectorRegistry

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

def process_metrics(app, metric_dir="./metrics", pattern=".metric"):
    directory = pathlib.Path(metric_dir)
    m = []

    for f in directory.iterdir():
        add_desc = True
        if f.is_file() and f.name.endswith(pattern):
            m_name = f.name.split('.')[0]
            with open(os.path.join(directory,f.name),'r') as mfile:
                for line in mfile:
                    split_line = line.split(';')
                    m_desc = split_line[0]
                    m_type = split_line[1]
                    m_comment = split_line[2]
                    m_label = split_line[3]
                    m_value = split_line[4]
                    if add_desc:
                        m.append(add_description(m_name, m_desc, m_type, m_comment))
                        add_desc = False
                    
                    m.append(add_metric(m_name, m_label, m_value))

        continue

    return m


def add_description(m_name,  m_desc, m_type, m_comment):
    template = "# HELP {0} {1}</br># TYPE {0} {2}</br># {3}</br>"

    return template.format(m_name, m_desc, m_type, m_comment)


def add_metric(m_name, m_label, m_value):
    template="{0}{{{1}}} {2}</br>"
    return template.format(m_name, m_label, m_value)

