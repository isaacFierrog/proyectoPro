from rest_framework import serializers
from .models import SensorModel


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorModel
        fields = '__all__'
        read_only_fields = ('id',)
