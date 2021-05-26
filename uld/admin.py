from django.contrib import admin
from .models import UldNumber


@admin.register(UldNumber)
class UldNumberAdmin(admin.ModelAdmin):
    list_display = [
        'unit_type',
        'unit_number',
        'unit_owner',
    ]
