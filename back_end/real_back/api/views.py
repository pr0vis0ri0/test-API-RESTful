# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from real_back.models import Departamento
# from .serializers import DepartamentoSerializer

# @api_view(['GET'])
# def lista_departamentos(request):
#     departamentos = Departamento.objects.all()
#     serializer = DepartamentoSerializer(departamentos, many=True)
#     return Response(serializer.data)
from rest_framework.viewsets import ModelViewSet
from real_back.models import Departamento
from real_back.api.serializers import DepartamentoSerializer

class DepartamentoApiViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()