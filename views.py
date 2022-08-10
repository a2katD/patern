from a2kat_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Aries:
    def __call__(self, request):
        return '200 OK', render('aries.html', data=request.get('data', None))


class Taurus:
    def __call__(self, request):
        return '200 OK', render('taurus.html', data=request.get('data', None))


class Gemini:
    def __call__(self, request):
        return '200 OK', render('gemini.html', data=request.get('data', None))


class Cancer:
    def __call__(self, request):
        return '200 OK', render('cancer.html', data=request.get('data', None))


class Leo:
    def __call__(self, request):
        return '200 OK', render('leo.html', data=request.get('data', None))


class Virgo:
    def __call__(self, request):
        return '200 OK', render('virgo.html', data=request.get('data', None))


class Libra:
    def __call__(self, request):
        return '200 OK', render('libra.html', data=request.get('data', None))


class Scorpio:
    def __call__(self, request):
        return '200 OK', render('scorpio.html', data=request.get('data', None))


class Sagitarius:
    def __call__(self, request):
        return '200 OK', render('sagitarius.html', data=request.get('data', None))


class Capricorn:
    def __call__(self, request):
        return '200 OK', render('capricorn.html', data=request.get('data', None))


class Aquarius:
    def __call__(self, request):
        return '200 OK', render('aquarius.html', data=request.get('data', None))


class Pisces:
    def __call__(self, request):
        return '200 OK', render('pisces.html', data=request.get('data', None))


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', 'Error 404. Page not found'
