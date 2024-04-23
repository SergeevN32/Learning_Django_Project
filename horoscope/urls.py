from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index, name='horoscope-index'),
    path('type', views_horoscope.get_info_about_type),
    path('type/<str:element>', views_horoscope.get_info_about_type_zodiac, name='horoscope_type-name'),
    path('<int:month>/<int:day>', views_horoscope.get_info_about_zodiac_by_date),
    path('<int:sign_zodiac>', views_horoscope.get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>', views_horoscope.get_info_about_zodiac, name='horoscope-name'),
]
