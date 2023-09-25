from django.contrib import admin
from .models import Film, Genre, Language, Country


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year_out', 'language', 'get_genre')


admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Country)

