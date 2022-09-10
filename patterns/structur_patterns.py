from time import time
from patterns.create_patterns import Logger


class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kw):
                start_time = time()
                result = method(*args, **kw)
                end_time = time()
                delta = end_time - start_time
                Logger.debug(f'{self.name} выполнялся {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)
