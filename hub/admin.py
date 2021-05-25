from django.contrib import admin
from .models import *
from flight.models import Flight


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = [
        'str_awb_owner',
        'str_awb_number',
        'origin',
        'destination',
        'awb_pcs',
        'awb_weight',
        'awb_vol',
        'str_shipment_type',
        'shc_code1',
        'shc_code2',
        'shc_code3',
        'shc_code4',
        'shc_code5',
        'handling',
        'inbound_flight',
    ]
    search_fields = ['str_awb_number']
