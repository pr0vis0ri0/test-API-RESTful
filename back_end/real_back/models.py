# Creación de modelos

from django.db import models

class Departamento (models.Model) :
    id_departamento = models.AutoField(primary_key=True)
    tipo_departamento = models.CharField(max_length=50)
    precio_departamento = models.IntegerField()
    direccion_departamento = models.CharField(max_length=50)
    metros_departamento = models.IntegerField()

class Reserva (models.Model) :
    id_departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField()
    