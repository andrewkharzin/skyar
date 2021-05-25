from rest_framework import viewsets
from .serializers import ShipmentSerializer
from .models import Shipment
from rest_framework.authentication import TokenAuthentication


class SRViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    authentication_classes = (TokenAuthentication, )
