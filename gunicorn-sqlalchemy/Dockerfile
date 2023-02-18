FROM ubuntu:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN pip3 install gunicorn paste python-multipart mysql-connector-python py-postgresql sqlalchemy pymysql
RUN pip3 install smart_open geoip2 boto3 google-api-python-client google-cloud-storage pyyaml
RUN rm -Rf /var/lib/apt/lists/*
ENV PORT=8081
ENV WSGI_DIR=/opt
ENV WSGI_APP=wsgi:application
COPY wsgi.py $WSGI_DIR
ENTRYPOINT gunicorn --bind=0.0.0.0:$PORT --workers=3 --chdir=$WSGI_DIR $WSGI_APP
EXPOSE $PORT
