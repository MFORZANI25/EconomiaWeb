from django.urls import path

from BlogEconomia.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogList.as_view(), name="Blog"),
    path('<int:pk>/', BlogDetalle.as_view(), name='Detail'),
    path('nuevo/', BlogCreacion.as_view(), name='New'),
    path('editar/<int:pk>/', BlogUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>/', BlogDelete.as_view(), name='Delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)