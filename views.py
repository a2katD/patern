from a2kat_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request.get('data', None))


class Aries:
    def __call__(self, request):
        return '200 OK', render('horoscope/aries.html', data=request.get('data', None))


class Taurus:
    def __call__(self, request):
        return '200 OK', render('horoscope/taurus.html', data=request.get('data', None))


class Gemini:
    def __call__(self, request):
        return '200 OK', render('horoscope/gemini.html', data=request.get('data', None))


class Cancer:
    def __call__(self, request):
        return '200 OK', render('horoscope/cancer.html', data=request.get('data', None))


class Leo:
    def __call__(self, request):
        return '200 OK', render('horoscope/leo.html', data=request.get('data', None))


class Virgo:
    def __call__(self, request):
        return '200 OK', render('horoscope/virgo.html', data=request.get('data', None))


class Libra:
    def __call__(self, request):
        return '200 OK', render('horoscope/libra.html', data=request.get('data', None))


class Scorpio:
    def __call__(self, request):
        return '200 OK', render('horoscope/scorpio.html', data=request.get('data', None))


class Sagitarius:
    def __call__(self, request):
        return '200 OK', render('horoscope/sagitarius.html', data=request.get('data', None))


class Capricorn:
    def __call__(self, request):
        return '200 OK', render('horoscope/capricorn.html', data=request.get('data', None))


class Aquarius:
    def __call__(self, request):
        return '200 OK', render('horoscope/aquarius.html', data=request.get('data', None))


class Pisces:
    def __call__(self, request):
        return '200 OK', render('horoscope/pisces.html', data=request.get('data', None))


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', 'Error 404. Page not found'
