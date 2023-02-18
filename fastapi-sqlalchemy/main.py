from fastapi import FastAPI, Request, Response
import traceback

app = FastAPI()
@app.get("/{path:path}")
def main(path, r: Request):

    try:

        message = "Welcome to FastAPI!  To use a custom entry point, set the APP and APP_DIR environment variables"
        return Response(
            status_code = 200,
            headers = {'Content-Type': "text/plain"},
            content = message
        )

    except:
        return Response(status_code = 500, content = traceback.format_exc())

