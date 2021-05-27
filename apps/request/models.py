from django.db import models
from apps.flight.models import *
from apps.hub.models import *
from apps.uld.models import *
from datetime import datetime


class TrRequest(models.Model):

    STATE_R_STATUS = (
        ('NW', 'NEW'),
        ('OTF', 'OKTOFWD'),
        ('RCD', 'REJECTED'),
        ('CCD', 'CANCELED')
    )
    trr_date = models.DateTimeField(default='', blank=True)
    title = models.CharField(null=True, blank=True, max_length=55)

    state_status = models.CharField(
        null=False, blank=False, default='NEW', max_length=36, choices=STATE_R_STATUS)
    is_completed = models.BooleanField(default=False)
    standby = models.BooleanField(default=True)
    trr_shipment = models.ForeignKey(
        Shipment, null=True, blank=True, on_delete=CASCADE, default='')
    units = models.ForeignKey(UldNumber, null=True,
                              blank=True, on_delete=CASCADE, default='')
    trr_arr_flight = models.ForeignKey(
        ArrFlight, null=True, blank=True, on_delete=CASCADE, default='')
    trr_dep_flight = models.ForeignKey(
        DepFlight, null=True, blank=True, on_delete=CASCADE, default='')
    description = models.TextField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
