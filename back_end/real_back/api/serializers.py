from rest_framework.serializers import ModelSerializer
from real_back.models import Departamento, Reserva

class DepartamentoSerializer (ModelSerializer):
    class Meta :
        model = Departamento
        fields = '__all__'

class ReservaSerializer (ModelSerializer):
    class Meta :
        model = Reserva
        fields = '__all__'