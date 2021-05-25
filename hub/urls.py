from django.urls import path, include
from rest_framework import routers
from .views import SRViewSet

router = routers.DefaultRouter()
router.register('Shipment', SRViewSet)

urlpatterns = [
    path('', include(router.urls))
]
