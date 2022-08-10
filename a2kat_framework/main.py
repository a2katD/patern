import quopri


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', 'Error 404. Page not found'


class Framework:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path.endswith('/'):
            path = path[:-1]

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        request = dict()
        for fronts in self.fronts:
            fronts(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
