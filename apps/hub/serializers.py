from rest_framework import serializers
from .models import Shipment
from apps.hub.models import *


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment, ArrFlight, DepFlight
        fields = [
            'str_shipment_type',
            'str_hndl_temp',
            'str_awb_owner',
            'str_awb_number',
            'awb_pcs',
            'awb_weight',
            'awb_vol',
            'origin',
            'destination',
            'shc_code1',
            'shc_code2',
            'shc_code3',
            'shc_code4',
            'shc_code5',
            'handling',
            'inbound_flight',
            'outbound_flight',

        ]
