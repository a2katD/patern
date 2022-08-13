from datetime import date
from views import *

routes = {
    '': Index(),
    '/contact': Contact(),
    '/aries': Aries(),
    '/taurus': Taurus(),
    '/gemini': Gemini(),
    '/cancer': Cancer(),
    '/leo': Leo(),
    '/virgo': Virgo(),
    '/libra': Libra(),
    '/scorpio': Scorpio(),
    '/sagitarius': Sagitarius(),
    '/capricorn': Capricorn(),
    '/aquarius': Aquarius(),
    '/pisces': Pisces(),
}


def date_time(request):
    request['data'] = date.today()


fronts = [date_time]
