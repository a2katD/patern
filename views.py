from a2kat_framework.templator import render

from patterns.create_patterns import Engine, Logger

site = Engine()
logging = Logger("views")


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Categories:
    def __call__(self, request):
        return '200 OK', render('categories.html', objects_list=site.categories)


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


# контроллер - список курсов
class CoursesList:
    def __call__(self, request):
        logging.info('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('course_list.html', objects_list=site.courses, name=category.name,
                                    id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'



# контроллер - создать курс
class CreateCourse:
    category_id = -1

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
            return '200 OK', render('course_list.html', objects_list=site.courses,
                                    name=category.name, id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))
                return '200 OK', render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# контроллер - создать категорию
class CreateCategory:
    def __call__(self, request):
        if request['method'] == 'POST':
            logging.info(f'POST-запрос {request}')
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 OK', render('categories.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


# контроллер - список категорий
class CategoryList:
    def __call__(self, request):
        logging.info('Список категорий')
        return '200 OK', render('categories.html', objects_list=site.categories)


# контроллер - копировать курс
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)
            self.category_id = int(request['request_params']['id'])
            category = site.find_category_by_id(int(self.category_id))

            return '200 OK', render('course_list.html', objects_list=site.courses, id=category.id, name=category.name)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
