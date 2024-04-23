from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from faker import Faker
import random


# Create your views here.

def people(request):
    fake = Faker('ru')
    people_list = [fake.name() for _ in range(10)]
    data = {
        'list': people_list,
    }
    return render(request, 'example/people.html', context=data)


def people_detail(request):
    fake = Faker('ru')
    people_list = [{'name': fake.name(), 'age': random.randint(20, 68), 'phone': fake.phone_number()} for _ in range(10)]
    data = {
        'list': people_list,
    }
    return render(request, 'example/people_detail.html', context=data)

def beautiful_table(request):
    return render(request, 'example/beautiful_table.html')