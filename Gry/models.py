from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Producent(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"
        #


class Gatunek(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"
        #


class Gry(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE, null=True)
    zdjecie = models.ImageField(upload_to='', default='temp.jfif')

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Gra"
        verbose_name_plural = "Gry"
        #


class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Gry, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.nazwa

    class Meta:
        verbose_name = "Gra użytkownika"
        verbose_name_plural = "Gry użytkownika"
        #


class UserWishGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Gry, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.nazwa

    class Meta:
        verbose_name = "Wymażona gra użytkownika"
        verbose_name_plural = "Wymażone gry użytkownika"
        #
