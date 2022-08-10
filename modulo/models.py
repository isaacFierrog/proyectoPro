from django.db import models


class ModuloModel(models.Model):
    mac = models.CharField(max_length=150)
    mina = models.CharField(max_length=150)
    area = models.CharField(max_length=150)

    def __str__(self):
        return self.mac