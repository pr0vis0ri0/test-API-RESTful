from django.db import models

class Region (models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=70)
    capital_region = models.CharField(max_length=30, default='')
    
    def __str__ (self):
        return (str(self.id_region) + ' ' + self.nombre_region)
    
    class Meta :
        ordering = ['id_region']
    
class Comuna (models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)
    id_region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    def __str__ (self):
        return (str(self.id_comuna) + ' ' + self.nombre_comuna)
    
    class Meta :
        ordering = ['id_comuna']

class TipoPropiedad (models.Model):
    id_tipo_propiedad = models.AutoField(primary_key=True)
    nombre_tipo_propiedad = models.CharField(max_length=20)

    def __str__(self):
        return (str(self.id_tipo_propiedad) + ' ' + self.nombre_tipo_propiedad)

    class Meta :
        ordering = ['id_tipo_propiedad']

class Propiedad (models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    valor_propiedad = models.IntegerField()
    es_arriendo = models.IntegerField()
    es_venta = models.IntegerField()
    id_tipo_propiedad = models.ForeignKey(TipoPropiedad, null=True, on_delete=models.SET_NULL)
    id_comuna = models.ForeignKey(Comuna, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id_propiedad)

    class Meta :
        ordering = ['id_propiedad']

class CaracteristicasPropiedad (models.Model):
    metros_totales = models.IntegerField(default=0)
    metros_utiles = models.IntegerField(default=0)
    cant_dormitorios = models.IntegerField()
    cant_banos = models.IntegerField()
    permite_mascotas = models.IntegerField()
    tiene_bodega = models.IntegerField()
    tiene_estacionamiento = models.IntegerField()
    id_propiedad = models.OneToOneField(Propiedad,null=True,on_delete=models.SET_NULL)

    class Meta :
        ordering = ['id_propiedad']

class Visita (models.Model):
    id_visita = models.AutoField(primary_key=True)
    dia_visita = models.DateField()
    hora_visita = models.TimeField()
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    telefono = models.CharField(max_length=11)
    id_propiedad = models.ForeignKey(Propiedad, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.id_visita

    class Meta :
        ordering = ['id_visita']