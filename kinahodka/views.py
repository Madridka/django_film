from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Film


class FilmView(View):
    def get(self, request):
        film = Film.objects.all()
        return render(request, 'home.html', {'film_list': film})
