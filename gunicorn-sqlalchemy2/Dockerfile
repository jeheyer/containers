FROM python:3.10-slim-bullseye
MAINTAINER johnnylingo
WORKDIR /tmp
RUN pip3 install --upgrade pip
RUN pip3 install gunicorn
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
ENV PORT=8081
ENV WSGI_DIR=/opt
ENV WSGI_APP=wsgi:application
ENV NUM_WORKERS=1
ENV NUM_THREADS=8
COPY wsgi.py $WSGI_DIR
ENTRYPOINT gunicorn -b 0.0.0.0:$PORT -w $NUM_WORKERS --threads=$NUM_THREADS --chdir=$WSGI_DIR $WSGI_APP
EXPOSE $PORT
