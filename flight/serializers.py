from rest_framework import serializers
from hub.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'f_type',
            'f_number',
            'f_registration'

        ]
