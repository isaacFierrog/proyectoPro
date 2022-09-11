from pydoc import describe
from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.titulo