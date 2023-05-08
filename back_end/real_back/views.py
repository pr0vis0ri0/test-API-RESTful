from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Departamento
from .serializers import DepartamentoSerializer

@api_view(['GET'])
def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    serializer = DepartamentoSerializer(departamentos, many=True)
    return Response(serializer.data)