from django.contrib import admin
from .models import Film, Genre, Language, Country

"""регистрация в админке вывода лист_дисплея. get_genre - отдельная функция в моделях, 
где через for выводятся все жанры, т.к. модель MtM. Если выводить страны - то так же через get_country"""


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year_out', 'language', 'get_genre')

"""остальным моделям нет смысла редактировать вывод, там простейшие данные"""
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Country)

