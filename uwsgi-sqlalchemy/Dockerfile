FROM ubuntu:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt -y install python3-pip
RUN pip3 install uwsgi paste python-multipart mysql-connector-python py-postgresql sqlalchemy pymysql
RUN pip3 install smart_open geoip2 boto3 google-api-python-client google-cloud-storage pyyaml
RUN rm -Rf /var/lib/apt/lists/*
ENV PORT=8080
ENV WSGI_DIR=/opt
ENV WSGI_FILE=wsgi.py
COPY $WSGI_FILE $WSGI_DIR
ENTRYPOINT cd $WSGI_DIR && uwsgi --http :$PORT --workers 3 --wsgi-file $WSGI_FILE --callable application --enable-threads
EXPOSE $PORT
