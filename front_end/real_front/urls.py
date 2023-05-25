from django.urls import path
from . import views

urlpatterns = [
    path('propiedades', views.propiedades),
]