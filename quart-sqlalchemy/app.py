from quart import Quart

app = Quart(__name__)

@app.route("/", defaults = {'path': ""})
@app.route("/<path:path>")
@app.route("/<string:path>")
def root(path):

    message = "Welcome to Quart!  Set QUART_APP to your custom entry point\n\n"
    return message, 200, {'Content-Type': "text/plain"}

if __name__ == '__main__':
    app.run(debug=True)
