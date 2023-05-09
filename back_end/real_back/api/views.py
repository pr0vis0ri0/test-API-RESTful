from rest_framework.viewsets import ModelViewSet
from real_back.models import Departamento
from real_back.api.serializers import DepartamentoSerializer

class DepartamentoApiViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()