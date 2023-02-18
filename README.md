# Just Some Containers I've Built

| Name                                         | Description                                | Base Image      | Docker Image                       |
|----------------------------------------------|--------------------------------------------|-----------------|------------------------------------|
| [flask2_sqlalchemy](flask2_sqlachemy)        | Flask 2.x on Python 3.10.x w/ SQL Alchemy  | `ubuntu:latest` | `johnnylingo/flask2-sqlalchemy`    | 
| [quart_sqlalchemy](quart_sqlachemy)          | Quart on Python 3.10.x w/ SQL Alchemy      | `ubuntu:latest` | `johnnylingo/quart-sqlalchemy`     |
| [fastapi_sqlalchemy](fastapi_sqlachemy)      | FastAPI on Python 3.10.x w/ SQL Alchemy    | `ubuntu:latest` | `johnnylingo/fastapi-sqlalchemy`   |
| [apache2-bind9](apache2-bind9)               | Apache 2.4 and Bind 9                      | `ubuntu:latest` | `johnnylingo/apache2-bind9`        | 
| [gunicorn-bare](gunicorn-bare)               | Gunicorn 20.x web server                   | `debian:latest` | `johnnylingo/gunicorn-bare`        | 
| [uwsgi-bare](uwsgi-bare)                     | UWSGI web server                           | `debian:latest` | `johnnylingo/uwsgi-bare`           | 
| [apache-mod-wsgi-bare](apache-mod-wsgi-bare) | Apache 2.4 web server w/ mod WSGI          | `debian:latest` | `johnnylingo/apache-mod-wsgi-bare` |

# Usage Instructions

In these examples, /opt/www/myapp.py is my WSGI entry point

## For Flask

```
FLASK_APP=/opt/www/myapp.py
```

## For Quart

```
QUART_APP=/opt/www/myapp.py
```

## For FastAPI and Starlette

```
APP_DIR=/opt/www
APP=myapp:app
```

## For Plain WSGI apps

```
WSGI_DIR=/opt/www
WSGI_FILE=wsgi.py
```

## For Apache

- Mount any custom configuration files in /etc/apache2/conf-enabled/
- Mount any custom virtual host files in /etc/apache2/sites-enabled/

```
# Example /etc/apache2/conf-enabled/mod_wsgi.conf
<IfModule mod_wsgi.c>
  AddHandler wsgi-script .wsgi
  WSGIPythonOptimize 1
  WSGILazyInitialization On
  WSGIApplicationGroup %{GLOBAL}
</IfModule>
```


