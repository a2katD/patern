from datetime import date


def date_time(request):
    request['date'] = date.today()


fronts = [date_time]
