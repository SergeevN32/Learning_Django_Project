from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('', views_week_days.index),
    path('<int:day>', views_week_days.get_info_about_week_day_by_number),
    path('<str:day>', views_week_days.get_info_about_week_day, name='week_days-name'),
]