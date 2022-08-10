from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


OPCIONES_MINA = (
    (1, 'HERMOSILLO'),
    (2, 'CANANEA')
)

OPCIONES_ZONA = (
    (1, 'ZONA A'),
    (2, 'ZONA B'),
    (3, 'ZONA C'),
    (4, 'ZONA D'),
)


class UsuarioManager(BaseUserManager):
    def _create_user(self, correo, nombre, apellido, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            correo=correo,
            nombre=nombre,
            apellido=apellido,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_user(self, correo, nombre, apellido, password=None, **extra_fields):
        return self._create_user(correo, nombre, apellido, password, False, False, **extra_fields)

    def create_superuser(self, correo, nombre, apellido, password=None, **extra_fields):
        return self._create_user(correo, nombre, apellido, password, True, True, **extra_fields)


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(
        'Correo del usuario',
        unique=True
    )
    nombre = models.CharField(
        'Nombre del usuario',
        max_length=100
    )
    apellido = models.CharField(
        'Apellido del usuario',
        max_length=100
    )
    mina = models.PositiveIntegerField(
        'Mina a la que es asignado el usuario',
        choices=OPCIONES_MINA,
        default=1
    )
    zona = models.PositiveIntegerField(
        'Zona de la mina a la que es asignado el usuario',
        choices=OPCIONES_ZONA,
        default=1
    )
    is_active = models.BooleanField(
        'Estado en el que se encuntra el usuario ACTIVO/INACTIVO',
        default=True
    )
    is_staff = models.BooleanField(
        'El usuario puede acceder a la vista de administrador',
        default=False
    )
    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ('nombre', 'apellido')

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'