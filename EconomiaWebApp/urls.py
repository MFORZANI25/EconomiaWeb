from django.urls import path

from EconomiaWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios', views.servicios, name="Servicios"),
    path('about/', views.acerca_de_mi, name="About"),
    path('mensaje/', views.mensaje, name="Mensaje"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
