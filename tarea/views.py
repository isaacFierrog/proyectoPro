from rest_framework.viewsets import ModelViewSet
from .serializers import TareaSerializer
from .models import Tarea


class TareaViewSet(ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()