# Generated by Django 4.1.3 on 2022-12-04 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0005_gatunek_gry_gatunek'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gry',
            old_name='Gatunek',
            new_name='gatunek',
        ),
    ]
