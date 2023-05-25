from rest_framework.serializers import ModelSerializer
from .models import Region, Comuna, TipoPropiedad, Propiedad, CaracteristicasPropiedad, Visita

class RegionSerializer (ModelSerializer):
    class Meta :
        model = Region
        fields = '__all__'

class ComunaSerializer (ModelSerializer):
    class Meta :
        model = Comuna
        fields = '__all__'

class TipoPropiedadSerializer (ModelSerializer):
    class Meta :
        model = TipoPropiedad
        fields = '__all__'

class PropiedadSerializer (ModelSerializer):
    class Meta :
        model = Propiedad
        fields = '__all__'

class CaracteristicasPropiedadSerializer (ModelSerializer):
    class Meta :
        model = CaracteristicasPropiedad
        fields = '__all__'

class VisitaSerializer (ModelSerializer):
    class Meta :
        model = Visita
        fields = '__all__'