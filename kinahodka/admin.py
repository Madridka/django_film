from django.contrib import admin
from .models import Film, Genre, Language, Country


admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
