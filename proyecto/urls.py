# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from web.views import VehiculoCreateView, VehiculoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subir-vehiculo/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('lista-vehiculos/', VehiculoListView.as_view(), name='vehiculo_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
