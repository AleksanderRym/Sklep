# Generated by Django 4.1.3 on 2022-12-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gry',
            options={'verbose_name': 'Gra', 'verbose_name_plural': 'Gry'},
        ),
        migrations.RemoveField(
            model_name='gry',
            name='gatunek',
        ),
    ]
