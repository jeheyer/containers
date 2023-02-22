Hypercorn 0.13.x web server, FastAPI 0.70.x, Python 3.8.x w/ SQL Alchemy + Postgresql / MySQL / MariaDB 

To set a custom entry point, use the APP_DIR and APP environment variables.  Example:
```
APP_DIR=/mycustompath
APP=main:app
```
In this example, /mycustompath/main.py is the Python file, and has this line:
```
app = FastAPI()
```
