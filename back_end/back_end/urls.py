from django.contrib import admin
from django.urls import path, include
from real_back import views
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Creamos un router y registramos nuestro viewset

router = DefaultRouter()
router.register(r"region", views.RegionViewSet)
router.register(r"comuna", views.ComunaViewSet)
router.register(r"tipo_propiedad", views.TipoPropiedadViewSet)
router.register(r"propiedad", views.PropiedadViewSet)
router.register(r"caracteristicas_propiedad", views.CaracteristicasPropiedadViewSet)
router.register(r"visitas", views.VisitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace = "rest_framework")),
    path('api/v1/schema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]