from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Film, Likes
from .forms import CommentsForm
from django.http import HttpResponse
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


def get_client_ip(request):
    """получение ip-адреса клиента. если ip нет, то ремоте_аддр это типа прокси"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    """добавление лайков. обращение к классу лайки по ip и id, 1 Ip = 1 лайк на pk
    если лайк уже поставлен то переведет на страницу заглушку
    если лайка нет, то к модели Likes.ip ип клиента прибавится 1, а потом уже выдаю count по конкретному фильм_ид
    """
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, film_id=pk)
            return HttpResponse('Лайк уже поставлен. Вернитесь назад')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.film_id = int(pk)
            new_like.save()
            return redirect(f'/movies/{pk}')

"""система с удалением лайка действует так: по ип клиента определяется ставил ли лайк
если ставил, то из модели Likes ип клиента удаляется, и каунт уменьшается на 1
если удалять лайк не надо, то показательно появится httpresponse заглушка"""
class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client, film_id=pk)
            lik.delete()
            return redirect(f'/movies/{pk}')
        except:
            return HttpResponse('Нечего удалять. Вернитесь назад')
