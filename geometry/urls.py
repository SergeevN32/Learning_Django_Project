from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views_geometry.get_rectangle_area),
    path('rectangle/<int:width>/<int:height>', views_geometry.get_rectangle_area, name='rectangle-name'),
    path('get_square_area/<int:width>', views_geometry.get_square_area),
    path('square/<int:width>', views_geometry.get_square_area, name='square-name'),
    path('get_circle_area/<int:radius>', views_geometry.get_circle_area),
    path('circle/<int:radius>', views_geometry.get_circle_area, name='circle-name'),
]