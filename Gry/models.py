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
    producent = models.ForeignKey(Producent,on_delete=models.CASCADE, null=True)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Gra"
        verbose_name_plural = "Gry"
        #

