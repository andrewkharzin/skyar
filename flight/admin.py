from django.contrib import admin
from .models import *


@admin.register(ArrFlight, DepFlight)
class ArrFlightAdmin(admin.ModelAdmin):
    list_display = [
        'f_type',
        'f_number',
        'f_registration',
    ]


class DepFlightAdmin(admin.ModelAdmin):
    list_display = [
        'f_type',
        'f_number',
        'f_registration',
    ]
