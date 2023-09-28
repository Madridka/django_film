from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Film, Comment
from .forms import CommentsForm

"""с помощью модуля View создание отображений(views)
в классе функция обязательно должна быть get"""


class FilmView(View):
    """вывод на главную страницу только общее количество фильмов"""
    def get(self, request):
        num_films = Film.objects.all().count()
        return render(request, 'home.html', context={'num_films': num_films})


class FilmListView(View):
    """вывод всего списка фильмов на отдельной странице"""
    def get(self, request):
        film = Film.objects.all()
        return render(request, 'movies.html', context={'film_list': film})


class FilmDetail(View):
    """вывод каждого отдельного фильма на отдельной странице"""
    def get(self, request, pk):
        movie = Film.objects.get(id=pk)
        return render(request, 'film_detail.html', context={'movie': movie})


class AddComment(View):
    """добавление комментариев и оценки"""
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.film_id = pk
            form.save()
        return redirect(f'/movies/{pk}')

