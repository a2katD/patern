import copy
import quopri
import datetime as DT
from patterns.behavioral_patterns import ConsoleWriter, Subject


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class Student(User):
    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher,
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class CoursePrototype:
    def clone(self):
        return copy.deepcopy(self)


class Course(CoursePrototype, Subject):
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []
        self.teachers = []
        super().__init__()

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)
        self.notify('student')

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
        teacher.courses.append(self)
        self.notify('teacher')


class VebunaryCourse(Course):
    def __init__(self, name, category):
        super().__init__(name, category)
        type_ = "Вебинар"


class BookCourse(Course):
    def __init__(self, name, category):
        super().__init__(name, category)
        type_ = "Книга"


class VideoCourse(Course):
    def __init__(self, name, category):
        super().__init__(name, category)
        type_ = "Ведиокурс"


class CourseFactory:
    types = {
        'vebinary': VebunaryCourse,
        'video': VideoCourse,
        'book': BookCourse,
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Category:
    auto_id = 0

    def __init__(self, name, category, category_head):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.category_head = category_head
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create(type_, name)

    @staticmethod
    def create_category(name, category=None, category_head=0):
        return Category(name, category, category_head)

    def find_category_by_id(self, id):
        for item in self.categories:
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')

    def get_student(self, name):
        for item in self.students:
            if item.name == name:
                return item

    def get_teacher(self, name):
        for item in self.teachers:
            if item.name == name:
                return item


class LogerProto(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']
        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=LogerProto):
    def __init__(self, name, writer=ConsoleWriter()):
        self.name = name
        self.writer = writer

    def error(self, text):
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        log = f'{now:{"%Y-%m-%d %H:%M:%S"}} log ERROR: {text}'
        self.writer.write(log)

    def info(self, text):
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        log = f'{now:{"%Y-%m-%d %H:%M:%S"}} log INFO: {text}'
        self.writer.write(log)

    def debug(self, text):
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        log = f'{now:{"%Y-%m-%d %H:%M:%S"}} log DEBUG: {text}'
        self.writer.write(log)
