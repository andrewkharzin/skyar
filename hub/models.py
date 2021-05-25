from django.db import models
from django.db.models.deletion import CASCADE
from flight.models import Flight

# class Request(models.Model):
# STATE_R_STATUS = (
#     ('NW', 'NEW'),
#     ('OTF', 'OKTOFWD'),
#     ('RCD', 'REJECTED'),
#     ('CCD', 'CANCELED')
# )

# state_status = models.CharField(
#     null=False, blank=False, default='NEW', max_length=36, choices=STATE_R_STATUS)
# is_completed = models.BooleanField(default=False)


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
        Flight, null=True, blank=True, on_delete=CASCADE, default='')

    # published = models.DateTimeField(blank=True,  null=True, default=None)

    def __str__(self):
        return self.str_awb_number


class SHC(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    shc_text = models.CharField(max_length=3)


# class UldNumber(models.Model):
#     UNIT_TYPES = (
#         ('PMC', 'PMC'),
#         ('PLA', 'PLA'),
#         ('AKE', 'AKE'),
#         ('PYB', 'PYB')
#     )
#     UNIT_OWNERS = (
#         ('ABC', 'R7')
#     )
#     unit_type = models.CharField(
#         max_length=3, null=True, blank=True, choices=UNIT_TYPES)
#     unit_number = models.CharField(max_length=5, null=True, blank=True)
#     unit_owner = models.CharField(
#         max_length=2, null=True, blank=True, choices=UNIT_OWNERS)

# class Flight(models.Model):
# inbnd_flit_date = models.DateField(null=True, blank=True)
#     inbnd_flit_nmb = models.CharField(
#         null=True, blank=False, default='', max_length=6)
#     outbnd_flit_nmb = models.CharField(
#         null=True, blank=False, default='', max_length=6)
#     outbnd_flit_date = models.DateField(null=True, blank=True)
