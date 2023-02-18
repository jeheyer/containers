Uvicorn 0.16 web server, FastAPI 0.70.1, Python 3.8.10 w/ SQL Alchemy + Postgresql / MySQL / MariaDB 

To set a custom entry point, use the APP_DIR and APP environment variables.  Example:
```
APP_DIR=/mycustompath
APP=myapp:app
```
In this example, /mycustompath/myapp.py is the Python file, and has this line:
```
app = FastAPI()
```
