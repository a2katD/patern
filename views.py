from a2kat_framework.templator import render

from patterns.create_patterns import Engine, Logger
from patterns.structur_patterns import AppRoute, Debug

site = Engine()
logging = Logger("views")
routes = {}


@AppRoute(routes=routes, url='')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/categories')
class Categories:
    @Debug(name='Categories')
    def __call__(self, request):
        return '200 OK', render('categories.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/contact')
class Contact:
    @Debug(name='Contact')
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/aries')
class Aries:
    @Debug(name='Aries')
    def __call__(self, request):
        return '200 OK', render('horoscope/aries.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/taurus')
class Taurus:
    @Debug(name='Taurus')
    def __call__(self, request):
        return '200 OK', render('horoscope/taurus.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/gemini')
class Gemini:
    @Debug(name='Gemini')
    def __call__(self, request):
        return '200 OK', render('horoscope/gemini.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/cancer')
class Cancer:
    @Debug(name='Cancer')
    def __call__(self, request):
        return '200 OK', render('horoscope/cancer.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/leo')
class Leo:
    @Debug(name='Leo')
    def __call__(self, request):
        return '200 OK', render('horoscope/leo.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/virgo')
class Virgo:
    @Debug(name='Virgo')
    def __call__(self, request):
        return '200 OK', render('horoscope/virgo.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/libra')
class Libra:
    @Debug(name='Libra')
    def __call__(self, request):
        return '200 OK', render('horoscope/libra.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/scorpio')
class Scorpio:
    @Debug(name='Scorpio')
    def __call__(self, request):
        return '200 OK', render('horoscope/scorpio.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/sagitarius')
class Sagitarius:
    @Debug(name='Sagitarius')
    def __call__(self, request):
        return '200 OK', render('horoscope/sagitarius.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/capricorn')
class Capricorn:
    @Debug(name='Capricorn')
    def __call__(self, request):
        return '200 OK', render('horoscope/capricorn.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/aquarius')
class Aquarius:
    @Debug(name='Aquarius')
    def __call__(self, request):
        return '200 OK', render('horoscope/aquarius.html', data=request.get('data', None))


@AppRoute(routes=routes, url='/pisces')
class Pisces:
    @Debug(name='Pisces')
    def __call__(self, request):
        return '200 OK', render('horoscope/pisces.html', data=request.get('data', None))


class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', 'Error 404. Page not found'


@AppRoute(routes=routes, url='/courses-list')
class CoursesList:
    @Debug(name='CoursesList')
    def __call__(self, request):
        logging.info('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('course_list.html', courses_list=site.courses, name=category.name,
                                    id=category.id, categories_list=site.categories)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AppRoute(routes=routes, url='/create-course')
class CreateCourse:
    category_id = -1

    @Debug(name='CreateCourse')
    def __call__(self, request):
        if request['method'] == 'POST':
            logging.info(f'POST-запрос {request}')
            data = request['data']
            name = data['name']
            course_type = data['course_type']
            name = site.decode_value(name)
            course_type = site.decode_value(course_type)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course(course_type, name, category)
                site.courses.append(course)
            return '200 OK', render('course_list.html', courses_list=site.courses,
                                    name=category.name, id=category.id, categories_list=site.categories)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))
                return '200 OK', render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


@AppRoute(routes=routes, url='/create-category')
class CreateCategory:
    @Debug(name='CreateCategory')
    def __call__(self, request):
        if request['method'] == 'POST':
            logging.info(f'POST-запрос {request}')
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_head = int(data['category_head'])
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category, category_head)
            site.categories.append(new_category)
            return '200 OK', render('categories.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


@AppRoute(routes=routes, url='/category-list')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logging.info('Список категорий')
        return '200 OK', render('categories.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/copy-course')
class CopyCourse:
    @Debug(name='CopyCourse')
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            name = Engine.decode_value(name)
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_name = Engine.decode_value(new_name)
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)
            self.category_id = int(request['request_params']['id'])
            category = site.find_category_by_id(int(self.category_id))

            return '200 OK', render('course_list.html', courses_list=site.courses, id=category.id, name=category.name,
                                    categories_list=site.categories)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
