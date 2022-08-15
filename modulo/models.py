from django.db import models


class ModuloModel(models.Model):
    MINAS = (
        ('HERMOSILLO', 'HERMOSILLO'),
        ('CANANEA', 'CANANEA'),
    )
    AREAS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    
    mac = models.CharField(max_length=150)
    mina = models.CharField(max_length=150, choices=MINAS, default='HERMOSILLO')
    area = models.CharField(max_length=150, choices=AREAS, default='A')

    def __str__(self):
        return self.mac