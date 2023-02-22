# Just Some Python-based Containers I've Built

| Name                | Framework    | Web Server       | Base Image                  | Docker Image                                                                                |
|---------------------|--------------|------------------|-----------------------------|---------------------------------------------------------------------------------------------|
| fastapi-sqlalchemy2 | FastAPI 0.92 | Uvicorn 0.20.x   | `python:3.10-slim-bullseye` | [johnnylingo/fastapi-sqlalchemy2](https://hub.docker.com/r/johnnylingo/fastapi-sqlalchemy2) |
| flask2-sqlalchemy2  | Flask 2.x    | Gunicorn 20.x    | `python:3.10-slim-bullseye` | [johnnylingo/flask2-sqlalchemy2](https://hub.docker.com/r/johnnylingo/flask2-sqlalchemy2)   |
| quart-sqlalchemy2   | Quart 0.18.x | Hypercorn 0.14.x | `python:3.10-slim-bullseye` | [johnnylingo/quart-sqlalchemy2](https://hub.docker.com/r/johnnylingo/quart-sqlalchemy2)     |
| uwsgi-sqlalchemy2   | None         | uwsgi 2.0.x      | `debian:bullseye-slim`      | [johnnylingo/uwsgi-sqlalchemy2](https://hub.docker.com/r/johnnylingo/uwsgi-sqlalchemy2)     |
| apache-mod-wsgi     | None         | Apache 2.4.54    | `debian:bullseye-slim`      | [johnnylingo/apache-mod-wsgi](https://hub.docker.com/r/johnnylingo/apache-mod-wsgi)         |

# Usage Instructions

In these examples, `/opt/www/myapp.py` is the WSGI entry point

## Flask

```
FLASK_APP=/opt/www/myapp.py
```

## Quart

```
QUART_APP=/opt/www/myapp.py
```

## FastAPI & Starlette

```
APP_DIR=/opt/www
APP=myapp:app
```

## Plain WSGI apps

```
WSGI_DIR=/opt/www
WSGI_FILE=myapp.py
```

## Apache

- Mount any custom configuration files in /etc/apache2/conf-enabled/
- Mount any custom virtual host files in /etc/apache2/sites-enabled/

Example config file

```
<Directory "/opt/www">
  AllowOverride None
  Require all granted
  Require method GET POST OPTIONS
</Directory>
<VirtualHost *:80>
  ServerName localhost
  ServerAdmin nobody@localhost
  DocumentRoot /var/www/html
  WSGIDaemonProcess wsgi_python python-path=/opt/www
  WSGIProcessGroup wsgi_python
  WSGIScriptAlias /myapp.wsgi /opt/www/myapp.py
</VirtualHost>
```
