from django.db import models


class Celulares (models.Model):
    modelo = models.CharField(max_length=45)
    fabricante = models.CharField(max_length=40)
    ano = models.IntegerField()

    def __str__(self):
        return self.modelo

