from rest_framework import viewsets
from .serializers import FlightSerializer
from .models import Flight
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SRViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
