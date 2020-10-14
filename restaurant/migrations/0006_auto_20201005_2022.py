# Generated by Django 3.1 on 2020-10-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20201005_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.IntegerField(choices=[(1, 'dinner'), (4, 'drinks'), (5, 'alcohol'), (2, 'lunch'), (6, 'other'), (3, 'starters')], verbose_name='Kategoria dania'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]