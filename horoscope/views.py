from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

signs_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

type_signs_dict = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"],
}

date_signs_dict = {
    1: {'capricorn': range(1, 21), 'aquarius': range(21, 32)},
    2: {'aquarius': range(1, 20), 'pisces': range(20, 30)},
    3: {'pisces': range(1, 21), 'aries': range(21, 32)},
    4: {'aries': range(1, 21), 'taurus': range(21, 31)},
    5: {'taurus': range(1, 22), 'gemini': range(22, 32)},
    6: {'gemini': range(1, 22), 'cancer': range(22, 31)},
    7: {'cancer': range(1, 23), 'leo': range(23, 32)},
    8: {'leo': range(1, 22), 'virgo': range(22, 32)},
    9: {'virgo': range(1, 23), 'libra': range(23, 31)},
    10: {'libra': range(1, 24), 'scorpio': range(24, 32)},
    11: {'scorpio': range(1, 23), 'sagittarius': range(23, 31)},
    12: {'sagittarius': range(1, 23), 'capricorn': range(23, 32)},
}


def index(request):
    zodiac_list = list(signs_dict)
    data = {
        'zodiacs': zodiac_list,
        'signs_dict': signs_dict,
    }
    return render(request, 'horoscope/index.html', context=data)


def get_info_about_zodiac_by_date(request, month: int, day: int):
    dict_day = date_signs_dict[month]
    for sign in dict_day:
        if day in dict_day[sign]:
            redirect_path = reverse('horoscope-name', args=[sign])
            return HttpResponseRedirect(redirect_path)


def get_info_about_type(request):
    type_zodiac_list = list(type_signs_dict)
    li_elements = ''
    for elem in type_zodiac_list:
        redirect_path = reverse('horoscope_type-name', args=[elem])
        li_elements += f"<li> <a href='{redirect_path}'>{elem.title()}</a></li>"
    response = f'''
            <ul>
                {li_elements}
            </ul>
            '''
    return HttpResponse(response)


def get_info_about_type_zodiac(request, element: str):
    type_zodiac_list = type_signs_dict[element]
    li_elements = ''
    for element in type_zodiac_list:
        redirect_path = reverse('horoscope-name', args=[element])
        li_elements += f"<li> <a href='{redirect_path}'>{element.title()}</a></li>"
    response = f'''
                <ul>
                    {li_elements}
                </ul>
                '''
    return HttpResponse(response)


def get_info_about_zodiac(request, sign_zodiac: str):
    description = signs_dict.get(sign_zodiac.lower(), None)
    zodiac_list = list(signs_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'sign_name': description.split()[0],
        'zodiacs': zodiac_list,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_by_number(request, sign_zodiac: int):
    zodiac_list = list(signs_dict)
    if sign_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')
    description = zodiac_list[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[description])
    return HttpResponseRedirect(redirect_url)
