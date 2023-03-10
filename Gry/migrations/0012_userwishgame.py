# Generated by Django 4.1.3 on 2023-01-09 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gry', '0011_usergame'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWishGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gry.gry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wymażona gra użytkownika',
                'verbose_name_plural': 'Wymażone gry użytkownika',
            },
        ),
    ]
