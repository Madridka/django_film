"""этот urls.py только для этого приложения.
в основном файле urls.py проекта через include ссылка сюда"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('list/', views.FilmListView.as_view(), name='list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
