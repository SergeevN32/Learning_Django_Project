from django.urls import path
from . import views as views_example

urlpatterns = [
    path('people', views_example.people),
    path('people_detail', views_example.people_detail),
    path('beautiful_table', views_example.beautiful_table),
]