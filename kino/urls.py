from django.contrib import admin
from django.urls import path, include
from kinahodka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kinahodka.urls'))
]
