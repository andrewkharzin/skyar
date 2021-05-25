from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            'str_shipment_type',
            'str_hndl_temp',
            'str_awb_owner',
            'str_awb_number',
            'awb_pcs',
            'awb_weight',
            'awb_vol',
        ]
