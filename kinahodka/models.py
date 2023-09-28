from django.db import models


"""полная база про фильм. 
4 модели сделаны charfield/textfield, 
2 модели сделаны отношением многие ко многим (manytomany), чтобы фильм мог иметь не только 1 жанр/страну
1 модель (язык) сделана, т.к. несколько фильмов могут быть на 1 языке"""

"""добавить вручную вводимое поле для оценки с КП"""


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


"""MtM отношение, чтобы можно было выбрать несколько жанров к 1ому фильму"""
class Genre(models.Model):
    genre = models.CharField(max_length=100,
                             verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre


"""связная таблица страна. MtM модель означает, что при создании модели Film, можно выбрать несколько стран"""
class Country(models.Model):
    country = models.CharField(max_length=20,
                               verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country


"""связная таблица 'страна'. FK модель означает, что при создании модели Film, язык может быть 1, 
но эти языке заранее заведены, чтобы выбрать в другом фильме такой же язык"""
class Language(models.Model):
    language = models.CharField(max_length=20,
                                verbose_name='Язык')

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.language


"""модель для комментариев. на каждой странице пользователь вводит имя, почту, оставляет коммент и ставить оценку 
от 1 до 5. пока что реализовано так, что пользователь неавторизован, оставляет комментарий с оценкой, и это все 
уходит на эту же страницу с фильмом вниз
личная оценка выводится рядом, но ни на что не влияет
но в теории можно брать все оценки, находить средний результат и выводить как оценка фильма пользователями сайта
через set.all.count можно вывести количество оценок, но хз как посчитать среднее"""
class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    email = models.EmailField()
    comment = models.TextField(max_length=1000, verbose_name='Текст комментария')
    rating = models.SmallIntegerField(verbose_name='Оценка', default=0)
    film = models.ForeignKey('Film', verbose_name='Фильм', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name} {self.film}'


"""система лайков под каждым фильмом. отслеживается ip адрес, поэтому накрутитки лайков не получится"""
class Likes(models.Model):
    ip = models.CharField(max_length=20, verbose_name='IP-адрес пользователя')
    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE)