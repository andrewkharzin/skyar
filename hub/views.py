from rest_framework import viewsets
from .serializers import ShipmentSerializer
from .models import Shipment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SRViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )