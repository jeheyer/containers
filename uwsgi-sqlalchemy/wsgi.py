
def application(environ, start_response):

    import traceback

    try:

        start_response('200 OK', [('Content-type', 'text/html')])
        message = "<html><body><h1>Welcome to WSGI</h1></body></html>\n"

    except:

        start_response('500 Internal Server Error', [('Content-type', 'text/plain')])
        message = str(traceback.format_exc())

    return [ message.encode('utf-8') ]
