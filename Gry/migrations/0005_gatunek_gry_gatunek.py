# Generated by Django 4.1.3 on 2022-12-04 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gry', '0004_gry_producent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
        ),
        migrations.AddField(
            model_name='gry',
            name='Gatunek',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gry.gatunek'),
        ),
    ]
