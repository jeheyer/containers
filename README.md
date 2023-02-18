# Just Some Containers I've Built

| Name                                                      | Description                                   | Base Image      | Docker Image                             |
|-----------------------------------------------------------|-----------------------------------------------|-----------------|------------------------------------------|
| [flask2_sqlalchemy](flask2_sqlachemy/)                    | Flask 2.x and Python 3.10.x                   | `ubuntu:latest` | `johnnylingo/flask2-sqlalchemy`          | 
| [apache-mod-wsgi-sqlalchemy](apache-mod-wsgi-sqlalchemy/) | Apache 2.4 w/ mod WSGI and Python 3.10.x      | `ubuntu:latest` | `johnnylingo/apache-mod-wsgi-sqlalchemy` | 
| [apache2-bind9](apache2-bind9/)                           | Apache 2.4 and Bind 9                         | `ubuntu:latest` | `johnnylingo/apache2-bind9`              | 
| [gunicorn-bare](gunicorn-bare/)                           | Gunicorn and some very basic packages         | `debian:latest` | `johnnylingo/gunicorn-bare`              | 
| [uwsgi-bare](uwsgi-bare/)                                 | UWSGI web server and some very basic packages | `debian:latest` | `johnnylingo/uwsgi-bare`                 | 

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


