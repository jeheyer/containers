FROM python:3.10-slim-bullseye
MAINTAINER johnnylingo
WORKDIR /tmp
RUN pip3 install quart hypercorn
COPY ../requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=8000
ENV QUART_DIR=/opt
ENV QUART_APP=app:app
COPY app.py $QUART_DIR
ENTRYPOINT cd $QUART_DIR && hypercorn --reload --bind 0.0.0.0:$PORT --workers 3 $QUART_APP
EXPOSE $PORT
