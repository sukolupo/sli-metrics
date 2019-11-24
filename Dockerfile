# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
#FROM python:alpine
FROM alpine:latest

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=sli-metrics Version=0.0.1
EXPOSE 80

WORKDIR /app
ADD . /app

RUN apk add --no-cache python3
RUN apk add --no-cache --virtual .build-deps  python3-dev gcc libc-dev libffi-dev openssl-dev py3-pip
 
# Using pip:
RUN python3 -m pip install -r requirements.txt
RUN apk del .build-deps
#CMD ["python3", "-m", "sli-metrics"]

CMD ["/usr/bin/uwsgi", "--http", ":80", "--manage-script-name", "--mount", "/app/sli-metrics=sli-metrics:app"]
#CMD ["/usr/bin/uwsgi", "--http", ":80", "--wsgi-file", "/app/sli-metrics/sli-metrics.py"]
 
# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "sli-metrics"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m sli-metrics"
