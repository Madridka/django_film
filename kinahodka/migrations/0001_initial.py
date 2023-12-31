# Generated by Django 4.0.4 on 2023-09-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Режиссер')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20, verbose_name='Язык')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('year_out', models.CharField(max_length=10, verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='Сюжет фильма')),
                ('author', models.CharField(max_length=50, verbose_name='Режиссер')),
                ('url_kp', models.URLField(verbose_name='Ссылка на KINOPOISK')),
                ('country', models.ManyToManyField(to='kinahodka.country', verbose_name='Страна')),
                ('genre', models.ManyToManyField(to='kinahodka.genre', verbose_name='Жанр')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinahodka.language', verbose_name='Язык')),
            ],
        ),
    ]
