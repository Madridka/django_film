from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=25,
                                  verbose_name='Имя режиссера')
    last_name = models.CharField(max_length=25,
                                 verbose_name='Фамилия режиссера')

    def __str__(self):
        return self.last_name


class Film(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название книги')
    year_out = models.CharField(max_length=10,
                                verbose_name='Год выпуска')
    description = models.CharField(max_length=1000,
                                   verbose_name='Сюжет фильма')

    author = models.ManyToManyField('Author',
                                    verbose_name='Режиссер')
    country = models.ManyToManyField('Country',
                                      verbose_name='Язык')

    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                verbose_name='Страна')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              verbose_name='Жанр')

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
