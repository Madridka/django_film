from django.contrib import admin
from .models import Film, Genre, Language, Country, Comment

"""регистрация в админке вывода лист_дисплея. get_genre - отдельная функция в моделях, 
где через for выводятся все жанры, т.к. модель MtM. Если выводить страны - то так же через get_country"""


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_out', 'language', 'get_genre')
    list_filter = ('year_out', 'language', 'genre')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'rating', 'name', 'comment')
    list_filter = ('film', 'rating', 'name')
    fieldsets = (
        ('Оценка', {'fields': ('rating', 'comment')}),
        ('Данные пользователя', {'fields': ('name', 'email')}),
    ) #в админке в разеделе статус отображение по field сетам

"""остальным моделям нет смысла редактировать вывод, там простейшие данные"""
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Country)


