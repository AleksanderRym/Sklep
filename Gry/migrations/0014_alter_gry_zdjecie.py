# Generated by Django 4.1.3 on 2023-01-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0013_alter_gry_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gry',
            name='zdjecie',
            field=models.ImageField(default='static/temp.png', upload_to=''),
        ),
    ]
