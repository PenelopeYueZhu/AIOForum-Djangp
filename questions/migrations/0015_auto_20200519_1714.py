# Generated by Django 3.0.4 on 2020-05-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20200519_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatequestion',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='publicquestion',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]