from django.contrib import admin

# Register your models here.
from .models import Departamento, Reserva
admin.site.register(Departamento)
admin.site.register(Reserva)