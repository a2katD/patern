import quopri
import sys
from a2kat_framework.request import PostRequests, GetRequests

sys.path.append('../')
from patterns.create_patterns import Logger

logging = Logger('framework')

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
        request = dict()
        method = environ['REQUEST_METHOD']
        request['method'] = method
        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            logging.info(f'POST-запрос: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        for fronts in self.fronts:
            fronts(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        result = {}
        for key, value in data.items():
            val_bytes = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode = quopri.decodestring(val_bytes).decode('UTF-8')
            result[key] = val_decode
        return result


class DebugApplication(Framework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = Framework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        Logger.debug(env)
        return self.application(env, start_response)


class FakeApplication(Framework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = Framework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
