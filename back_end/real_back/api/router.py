from rest_framework.routers import DefaultRouter
from real_back.api.views import DepartamentoApiViewSet

router_departamentos = DefaultRouter()

router_departamentos.register(prefix='get',basename='get', 
                              viewset=DepartamentoApiViewSet)