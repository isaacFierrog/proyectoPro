from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorSerializer
from .models import SensorModel
from modulo.models import ModuloModel



class SensorListView(ListView):
    model = SensorModel
    queryset = SensorModel.objects.all()
    template_name = 'sensor/listar_sensor.html'


class SensorViewSet(ModelViewSet):
    serializer_class = SensorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        modulo = ModuloModel.objects.filter(mac=request.data.pop('modulo')).first()
        sensor_serializer = self.get_serializer(
            data=request.data['valores'],
            many=True
        )

        if sensor_serializer.is_valid():
            print('VALORES VALIDADOS')
            for sensor_data in sensor_serializer.data:
                sensor_data.pop('modulo')
                self.get_serializer().Meta.model.objects.create(
                    modulo=modulo,
                    **sensor_data
                )
            
            return Response({
                'mensaje': 'Registros creados'
            })


        return Response({
            'mensaje': 'Hola'
        })