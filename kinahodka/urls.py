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
    # path('rating/<int:pk>/', views.AddRating.as_view(), name='add_rating'),
    # path('review/<int:pk>/rating', views.Average_Rating.as_view(), name='average_rating'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
