from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin
from .models import *

# creación de admin : python manage.py createsuperuser
# user: admin correo: cualquiera pass: admin

# Register your models here.

# https://django-import-export.readthedocs.io/en/

# Se añadió un feat llamado django-import-export el cual se instala con pip3 install django-import-export
# y permite importar o exportar las tablas de la base de datos que se maneja de forma nativa con sqlite3
# también se les añadieron campos de búsqueda al admin para poder buscar información.

# A continuación también se detallan algunas de las funcionalidades.

# Los resources se utilizan para definir la importación y exportación de las distintas tablas,
# en esta se pueden hacer validaciones, como si la instancia importada ya existe que la salte,
# entr otras.

# list_filster() Te añade un filtro a la derecha del sitio pero lo hace por cada campos que tú agregues
# por lo cual considero que no sirve mucho, a menos que sea en casos precisos como podría ser los departamentos, 
# para filtrar por tipo_propiedad ya que en otros casos tendrás mil filtros a la derecha.

# search_fields considera todos los campos dentro de la lista y permite 
# hacer búsquedas en la base de datos con estos campos.
class RegionResource(ModelResource):
    class Meta :
        model = Region
        import_id_fields = ['id_region']
        fields = ('id_region', 
                  'nombre_region', 
                  'capital_region')

class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [RegionResource]
    list_display = ('id_region',
                    'nombre_region',
                    'capital_region')
    search_fields = ('id_region',
                     'nombre_region',
                     'capital_region')

class ComunaResource(ModelResource):
    id_region = fields.Field(
        column_name='id_region',
        attribute='id_region',
        widget = ForeignKeyWidget(Region, field = 'id_region'))

    class Meta :
        model = Comuna
        import_id_fields = ['id_comuna']
        fields = ('id_comuna', 
                  'nombre_comuna', 
                  'id_region')

class ComunaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ComunaResource]
    list_display = ('id_comuna',
                    'nombre_comuna',
                    'id_region')
    search_fields = ('id_comuna',
                      'nombre_comuna',
                      'id_region')

class TipoPropiedadResource(ModelResource):
    class Meta :
        model = TipoPropiedad
        import_id_fields = ['id_tipo_propiedad']
        fields = ('id_tipo_propiedad',
                  'nombre_tipo_propiedad')

class TipoPropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [TipoPropiedadResource]
    list_display = ('id_tipo_propiedad',
                    'nombre_tipo_propiedad')
    search_fields = ('id_tipo_propiedad',
                    'nombre_tipo_propiedad')

class PropiedadResource (ModelResource):
    id_tipo_propiedad = fields.Field(
        column_name='id_tipo_propiedad',
        attribute='id_tipo_propiedad',
        widget=ForeignKeyWidget(TipoPropiedad, field='id_tipo_propiedad'))
    id_comuna = fields.Field(
        column_name='id_comuna',
        attribute='id_comuna',
        widget = ForeignKeyWidget(Comuna, field='id_comuna'))
    class Meta :
        model = Propiedad
        import_id_fields = ['id_propiedad']
        fields = ('id_propiedad',
                  'valor_propiedad',
                  'es_arriendo',
                  'es_venta',
                  'id_tipo_propiedad',
                  'id_comuna')

class PropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [PropiedadResource]
    list_display = ('id_propiedad',
                    'valor_propiedad',
                    'es_arriendo',
                    'es_venta',
                    'id_tipo_propiedad',
                    'id_comuna')
    search_fields = ('id_propiedad',
                    'valor_propiedad',
                    'es_arriendo',
                    'es_venta',
                    'id_tipo_propiedad',
                    'id_comuna')

class CaracteristicasPropiedadResource (ModelResource):
    id_propiedad = fields.Field(
        column_name='id_propiedad',
        attribute='id_propiedad',
        widget=ForeignKeyWidget(Propiedad, field= 'id_propiedad')
    )
    class Meta:
        model = CaracteristicasPropiedad
        fields = ('metros_totales',
                  'metros_utiles',
                  'cant_dormitorios',
                  'cant_banos',
                  'permite_mascotas',
                  'tiene_bodega',
                  'tiene_estacionamiento',
                  'id_propiedad')

class CaracteristicasPropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [CaracteristicasPropiedadResource]
    list_display = ('metros_totales',
                    'metros_utiles',
                    'cant_dormitorios',
                    'cant_banos',
                    'permite_mascotas',
                    'tiene_bodega',
                    'tiene_estacionamiento',
                    'id_propiedad')
    search_fields =('metros_totales',
                    'metros_utiles',
                    'cant_dormitorios',
                    'cant_banos',
                    'permite_mascotas',
                    'tiene_bodega',
                    'tiene_estacionamiento',
                    'id_propiedad')

class VisitaResource (ModelResource):
    id_propiedad = fields.Field(
        column_name='id_propiedad',
        attribute='id_propiedad',
        widget=ForeignKeyWidget(Propiedad, field= 'id_propiedad')
    )
    class Meta:
        model = CaracteristicasPropiedad
        import_id_fields = ['id_visita']
        fields = ('id_visita',
                  'dia_visita',
                  'hora_visita',
                  'nombre_completo',
                  'rut',
                  'correo',
                  'telefono',
                  'id_propiedad')

class VisitaAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [VisitaResource]
    list_display = ('id_visita',
                    'dia_visita',
                    'hora_visita',
                    'nombre_completo',
                    'rut',
                    'correo',
                    'telefono',
                    'id_propiedad')
    search_fields = ('id_visita',
                    'dia_visita',
                    'hora_visita',
                    'nombre_completo',
                    'rut',
                    'correo',
                    'telefono',
                    'id_propiedad')
    

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(TipoPropiedad, TipoPropiedadAdmin)
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(CaracteristicasPropiedad, CaracteristicasPropiedadAdmin)
admin.site.register(Visita, VisitaAdmin)