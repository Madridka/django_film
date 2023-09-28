# Generated by Django 4.0.4 on 2023-09-28 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kinahodka', '0009_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Оценка')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinahodka.film', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]