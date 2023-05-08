from rest_framework import serializers
from .models import Departamento, Reserva

class DepartamentoSerializer (serializers.ModelSerializer):
    class Meta :
        model = Departamento
        fields = '__all__'

class ReservaSerializer (serializers.ModelSerializer):
    class Meta :
        model = Reserva
        fields = '__all__'