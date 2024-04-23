from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

day_dict = {
    'monday': "Список дел на понедельник",
    'tuesday': "Список дел на вторник",
    'wednesday': "Список дел на среду",
    'thursday': "Список дел на четверг",
    'friday': "Список дел на пятницу",
    'saturday': "Список дел на субботу",
    'sunday': "Список дел на воскресенье",
}


def index(request):
    return render(request, 'week_days/index.html')

def get_info_about_week_day(request, day: str):
    description = day_dict.get(day.lower(), None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Такого дня недели нет - {day}")


def get_info_about_week_day_by_number(request, day: int):
    day_list = list(day_dict)
    if day > len(day_list):
        return HttpResponseNotFound(f"Неверный номер дня - {day}")
    description = day_list[day - 1]
    redirect_url = reverse(viewname='week_days-name', args=[description])
    return HttpResponseRedirect(redirect_url)

