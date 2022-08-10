from django.db import models
from modulo.models import ModuloModel


class SensorModel(models.Model):
    modulo = models.ForeignKey(
        ModuloModel, 
        on_delete=models.CASCADE,
        related_name='sensores',
        blank=True,
        null=True
    )
    sensor = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    valor = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.sensor
