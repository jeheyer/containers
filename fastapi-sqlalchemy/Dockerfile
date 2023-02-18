FROM debian:latest
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt -y install python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install fastapi hypercorn 
RUN pip3 install paste python-multipart mysql-connector-python py-postgresql sqlalchemy pymysql
RUN pip3 install smart_open geoip2 boto3 google-api-python-client google-cloud-storage pyyaml
RUN rm -Rf /var/lib/apt/lists/*
ENV APP_DIR=/opt
ENV APP=main:app
ENV PORT=8000
ENV NUM_WORKERS=3
COPY main.py $APP_DIR
ENTRYPOINT cd $APP_DIR && hypercorn --reload --bind 0.0.0.0:$PORT --workers $NUM_WORKERS $APP
EXPOSE $PORT
