import sys
from wsgiref.simple_server import make_server
from a2kat_framework.main import Framework, DebugApplication
from urls import fronts
from views import routes
from patterns.create_patterns import Logger

logging = Logger("runner")
DEBUG = False

for param in sys.argv:
    if param == '-debug' or param == '-d':
        DEBUG = True

if DEBUG:
    application = DebugApplication(routes, fronts)
else:
    application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    logging.info("Запуск на порту 8080...")
    httpd.serve_forever()
