# Generated by Django 4.1.3 on 2023-01-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0017_alter_gry_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gry',
            name='zdjecie',
            field=models.ImageField(default='temp.jfif', upload_to=''),
        ),
    ]
