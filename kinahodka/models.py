from django.db import models


# class Author(models.Model):
#     author = models.CharField(max_length=50,
#                               verbose_name='Режиссер')
#
#     def __str__(self):
#         return self.author


class Film(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название фильма')
    year_out = models.CharField(max_length=10,
                                verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Сюжет фильма')

    author = models.CharField(max_length=50,
                              verbose_name='Режиссер')

    genre = models.ManyToManyField('Genre',
                                   verbose_name='Жанр')
    country = models.ManyToManyField('Country',
                                     verbose_name='Страна')

    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Язык')

    url_kp = models.URLField(verbose_name='Ссылка на KINOPOISK')

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=100,
                             verbose_name='Жанр')

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=20,
                                verbose_name='Язык')

    def __str__(self):
        return self.language


class Country(models.Model):
    country = models.CharField(max_length=20,
                               verbose_name='Страна')

    def __str__(self):
        return self.country
