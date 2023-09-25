from django.urls import path
from . import views
"""этот urls.py только для этого приложения. 
в основном файле urls.py проекта через include ссылка сюда"""
urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('list/', views.FilmListView.as_view(), name='list')
]