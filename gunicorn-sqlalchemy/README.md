Simple Gunicorn 20.x web server, Python 3.10.x built on Ubuntu

To use, set WSGI_DIR and WSGI_APP to your entry point.  

For example, to use /opt/www/wsgi.py
```
WSGI_DIR=/opt/www
WSGI_APP=wsgi:application
```
