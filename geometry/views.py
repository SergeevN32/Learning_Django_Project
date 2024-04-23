from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.

def get_rectangle_area(request, width: int, height: int) -> int:
    redirect_url = reverse(viewname='rectangle-name', args=[width, height])
    if 'get_' in request.path:
        return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int) -> int:
    redirect_url = reverse(viewname='square-name', args=[width])
    if 'get_' in request.path:
        return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width ** 2}")
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int) -> float:
    redirect_url = reverse(viewname='circle-name', args=[radius])
    if 'get_' in request.path:
        return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f"Площадь круга радиусом {radius} равна {pi * radius ** 2}")
    return render(request, 'geometry/circle.html')
