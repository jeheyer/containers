
def application(environ, start_response):

    import traceback

    try:

        start_response('200 OK', [('Content-type', 'text/html')])
        return [ "Welcome to WSGI".encode('utf-8') ]

    except:

        start_response('500 Internal Server Error', [('Content-type', 'text/plain')])
        return [ str(traceback.format_exc()).encode('utf-8') ]
