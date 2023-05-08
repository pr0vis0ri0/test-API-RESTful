from django.urls import path
from real_back.views import lista_departamentos
# Create your views here.
urlpatterns = [
    path('api/departamentos/', lista_departamentos, name='departamentos')
]
