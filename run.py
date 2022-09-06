from wsgiref.simple_server import make_server

from a2kat_framework.main import Framework
from urls import routes, fronts
from patterns.create_patterns import Logger

logging = Logger("runner")

application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    logging.info("Запуск на порту 8080...")
    httpd.serve_forever()
