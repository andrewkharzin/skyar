from django.db import models
from django.db.models.deletion import CASCADE
from flight.models import *
from uld.models import UldNumber


class Shipment(models.Model):
    SHC_CODES = (
        ('ICE', 'ICE'),
        ('MAG', 'MAG'),
        ('ELI', 'ELI'),
        ('COL', 'COL'),
        ('ERT', 'ERT'),
        ('CRT', 'CRT'),
        ('NFR', 'NFR'),
        ('ACT', 'ACT')
    )

    str_shipment_type = models.CharField(
        null=False, blank=False, max_length=55, default='TTSP')
    str_awb_owner = models.CharField(
        null=False, blank=False, max_length=3, default='001')
    str_awb_number = models.CharField(
        null=False, blank=False, max_length=11, default='00000001')
    awb_pcs = models.IntegerField(blank=True, null=True)
    awb_weight = models.DecimalField(
        blank=True, null=True, max_digits=7, decimal_places=2)
    awb_vol = models.DecimalField(
        blank=True, null=True, max_digits=4, decimal_places=3)
    origin = models.CharField(null=False, blank=False,
                              max_length=3, default='XXX')
    destination = models.CharField(
        null=False, blank=False, max_length=3, default='XXX')
    shc_code1 = models.CharField(
        null=True, blank=True, max_length=3, default='', choices=SHC_CODES)
    shc_code2 = models.CharField(
        null=True, blank=True, max_length=3, default='', choices=SHC_CODES)
    shc_code3 = models.CharField(
        null=True, blank=True, max_length=3, default='', choices=SHC_CODES)
    shc_code4 = models.CharField(
        null=True, blank=True, max_length=3, default='', choices=SHC_CODES)
    shc_code5 = models.CharField(
        null=True, blank=True, max_length=3, default='', choices=SHC_CODES)
    handling = models.TextField(blank=True, null=True, default='')
    inbound_flight = models.ForeignKey(
        ArrFlight, null=True, blank=True, on_delete=CASCADE, default='')
    outbound_flight = models.ForeignKey(
        DepFlight, null=True, blank=True, on_delete=CASCADE, default='')
    uld = models.ForeignKey(UldNumber, null=True,
                            blank=True, on_delete=CASCADE, default='')

    def __str__(self):
        return self.str_awb_number


# class SHC(models.Model):
#     shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
#     shc_text = models.CharField(max_length=3)

