FROM debian:bullseye-slim
MAINTAINER johnnylingo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN rm -Rf /var/lib/apt/lists/*
WORKDIR /tmp
RUN pip3 install uwsgi
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=8080
ENV WSGI_DIR=/opt
ENV WSGI_FILE=wsgi.py
COPY $WSGI_FILE $WSGI_DIR
ENTRYPOINT cd $WSGI_DIR && uwsgi --http :$PORT --workers 3 --wsgi-file $WSGI_FILE --callable application --enable-threads
EXPOSE $PORT
