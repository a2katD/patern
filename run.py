from wsgiref.simple_server import make_server

from a2kat_framework.main import Framework
from urls import routes, fronts

application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    httpd.serve_forever()
