FROM python:3.10-slim-bullseye
MAINTAINER johnnylingo
WORKDIR /tmp
RUN pip3 install hypercorn fastapi 
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=8000
ENV APP_DIR=/opt
ENV APP=main:app
ENV NUM_WORKERS=3
COPY main.py $APP_DIR
ENTRYPOINT cd $APP_DIR && hypercorn --reload --bind 0.0.0.0:$PORT --workers $NUM_WORKERS $APP
EXPOSE $PORT
