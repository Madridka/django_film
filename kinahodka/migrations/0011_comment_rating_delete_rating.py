# Generated by Django 4.0.4 on 2023-09-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinahodka', '0010_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Оценка'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
