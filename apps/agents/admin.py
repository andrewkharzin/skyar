from django.contrib import admin
from apps.agents.models import AirlineAgent, GroundAgent


@admin.register(AirlineAgent, GroundAgent)
class AirlineAgentAdmin(admin.ModelAdmin):
    list_display = [
        'user'
    ]


class GroundAgentAdmin(admin.ModelAdmin):
    list_display = [
        'user'
    ]
