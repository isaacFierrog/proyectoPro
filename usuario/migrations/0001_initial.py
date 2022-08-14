# Generated by Django 4.1 on 2022-08-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo del usuario')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del usuario')),
                ('mina', models.PositiveIntegerField(choices=[(1, 'HERMOSILLO'), (2, 'CANANEA')], default=1, verbose_name='Mina a la que es asignado el usuario')),
                ('zona', models.PositiveIntegerField(choices=[(1, 'ZONA A'), (2, 'ZONA B'), (3, 'ZONA C'), (4, 'ZONA D')], default=1, verbose_name='Zona de la mina a la que es asignado el usuario')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado en el que se encuntra el usuario ACTIVO/INACTIVO')),
                ('is_staff', models.BooleanField(default=False, verbose_name='El usuario puede acceder a la vista de administrador')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]