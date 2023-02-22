FROM python:3.10-slim-bullseye
MAINTAINER johnnylingo
WORKDIR /tmp
RUN pip3 install --upgrade pip
RUN pip3 install Flask-SQLAlchemy gunicorn
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=8081
ENV FLASK_DIR=/opt
ENV FLASK_APP=app:app
ENV NUM_WORKERS=1
ENV NUM_THREADS=8
COPY app.py $FLASK_DIR
ENTRYPOINT gunicorn -b 0.0.0.0:$PORT -w $NUM_WORKERS --threads=$NUM_THREADS --chdir=$FLASK_DIR $FLASK_APP
EXPOSE $PORT
