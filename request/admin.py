from django.contrib import admin
from .models import *
from flight.models import *


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
        'created_at',
        'updated_at',

    ]
    search_fields = ['units']
