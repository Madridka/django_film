# Generated by Django 4.0.4 on 2023-09-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinahodka', '0005_alter_rating_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(max_length=2, verbose_name='Оценка'),
        ),
    ]