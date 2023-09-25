from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Film

"""с помощью модуля View создание отображений(views)
в классе функция обязательно должна быть get"""


class FilmView(View):
    def get(self, request):
        num_films = Film.objects.all().count()
        return render(request, 'home.html', context={'num_films': num_films})


class FilmListView(View):
    def get(self, request):
        film = Film.objects.all()
        return render(request, 'film_list.html', context={'film_list': film})
