"""этот urls.py только для этого приложения.
в основном файле urls.py проекта через include ссылка сюда"""

from django.urls import path
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    # во filmview ничего нет по сути, кроме каунта фильмов, поэтому выдается пустой home.html

    path('movies/', views.FilmListView.as_view(), name='movies'),
    #выводится movies.html,  context = Film.objects.all()

    path('movies/<int:pk>/', views.FilmDetail.as_view(), name='film_detail'),
    # выводится страница film_detail.html, где context = movie by id

    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    # по сути ничего не выводится, идет работа с вьюшкой AddComment,
    # передается post-запрос по form.is_valid, через форму CommentForm,
    # а она через модель Comment по field

    path('movies/<int:pk>/add_like', views.AddLike.as_view(), name='add_like'),
    path('movies/<int:pk>/del_like', views.DelLike.as_view(), name='del_like'),
    # в этих 2 path идет обработка вьюшек addlike и dellike, которые через связь по ip клиента
    # либо добавляют этот самый ip клиента в базу, для последующего count лайков

    path('add_film/', views.add_film, name='add_film'),
    url(r'^movies/update/(?P<pk>\d+)$', views.FilmUpdate.as_view(), name='film_update'),

    path("random/", views.random_page, name="random"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
