from rest_framework import serializers
from .models import ModuloModel


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloModel
        fields = '__all__'
        read_only_fields = ('id',)