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
    '/categories': Categories(),

    '/courses-list': CoursesList(),
    '/create-course': CreateCourse(),
    '/create-category': CreateCategory(),
    '/category-list': CategoryList(),
    '/copy-course': CopyCourse()
}


def date_time(request):
    request['date'] = date.today()


fronts = [date_time]
