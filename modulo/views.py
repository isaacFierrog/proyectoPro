from rest_framework.viewsets import ModelViewSet
from .serializers import ModuloSerializer


class ModuloViewSet(ModelViewSet):
    serializer_class = ModuloSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()