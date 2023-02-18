FROM ubuntu:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt -y install python3-pip 
RUN pip3 install quart hypercorn
RUN pip3 install paste python-multipart mysql-connector-python py-postgresql sqlalchemy pymysql
RUN pip3 install smart_open geoip2 boto3 google-api-python-client google-cloud-storage pyyaml
RUN rm -Rf /var/lib/apt/lists/*
ENV PORT=8000
ENV QUART_DIR=/opt
ENV QUART_APP=app:app
COPY app.py $QUART_DIR
ENTRYPOINT cd $QUART_DIR && hypercorn --reload --bind 0.0.0.0:$PORT --workers 3 $QUART_APP
EXPOSE $PORT
