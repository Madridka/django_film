"""этот urls.py только для этого приложения.
в основном файле urls.py проекта через include ссылка сюда"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('movies/', views.FilmListView.as_view(), name='movies'),
    path('movies/<int:pk>/', views.FilmDetail.as_view(), name='film_detail'),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('movies/<int:pk>/add_like', views.AddLike.as_view(), name='add_like'),
    path('movies/<int:pk>/del_like', views.DelLike.as_view(), name='del_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
