from django.contrib import admin
from .models import *
from apps.flight.models import *
from apps.hub.models import *


@admin.register(TrRequest)
class TrrAdmin(admin.ModelAdmin):
    list_display = [
        'trr_date',
        'title',
        'state_status',
        'trr_shipment',
        'units',
        'trr_arr_flight',
        'trr_dep_flight',
        'description',
        'standby',
        'is_completed',
        'is_approved',
        # 'created_at',
        # 'updated_at',
        'user',

    ]
    list_display_links = [
        'trr_shipment',
        'trr_arr_flight',
        'trr_dep_flight',
    ]
    search_fields = ['units']
