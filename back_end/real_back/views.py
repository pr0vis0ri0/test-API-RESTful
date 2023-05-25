from .models import Region, Comuna, TipoPropiedad, Propiedad, CaracteristicasPropiedad, Visita
from .serializers import RegionSerializer, ComunaSerializer, PropiedadSerializer, TipoPropiedadSerializer, CaracteristicasPropiedadSerializer, VisitaSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
            detail=False, 
            methods=['GET'],
            url_path=r'filtroRegiones/(?P<id_region>\d+)')
    def filtroRegiones(self, request, id_region):
        queryset = Comuna.objects.filter(id_region = id_region)
        serializer_class = ComunaSerializer(queryset, many = True)
        return JSONResponse(serializer_class.data)

class TipoPropiedadViewSet(viewsets.ModelViewSet):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer
    permission_classes = [permissions.IsAuthenticated]

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    permission_classes = [permissions.IsAuthenticated]

class CaracteristicasPropiedadViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasPropiedad.objects.all()
    serializer_class = CaracteristicasPropiedadSerializer
    permission_classes = [permissions.IsAuthenticated]

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
    permission_classes = [permissions.IsAuthenticated]