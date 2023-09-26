from django.db import models

"""был класс про Режиссеров, но удалил, т.к. нет смысла добавлять фамилии режиссеров в БД, 
# можно просто оставить как текстовое поле"""
# class Author(models.Model):
#     author = models.CharField(max_length=50,
#                               verbose_name='Режиссер')
#
#     def __str__(self):
#         return self.author

"""полная база про фильм. 
4 модели сделаны charfield/textfield, 
2 модели сделаны отношением многие ко многим (manytomany), чтобы фильм мог иметь не только 1 жанр/страну"""


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

    img = models.ImageField(verbose_name='Постер', upload_to='image/%Y')

    def get_genre(self):
        return ', '.join([str(g) for g in self.genre.all()])
        #функция для вывода жанров, т.к. genre manytomany и в админке не работает одиночный вывод

    def get_country(self):
        return ', '.join([str(c) for c in self.country.all()])
        #так же функция для вывода списка всех стран

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        #класс мета - данные о данных, чтобы в админке выводилось не Films, а Фильмы

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=100,
                             verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=20,
                                verbose_name='Язык')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.language


class Country(models.Model):
    country = models.CharField(max_length=20,
                               verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country
