from django.db import models


class UldNumber(models.Model):
    UNIT_TYPES = (
        ('PMC', 'PMC'),
        ('PLA', 'PLA'),
        ('AKE', 'AKE'),
        ('PYB', 'PYB')
    )
    UNIT_OWNERS = (
        ('ABC', 'R7'),
    )
    unit_type = models.CharField(
        max_length=3, null=True, blank=True, choices=UNIT_TYPES)
    unit_number = models.CharField(max_length=5, null=True, blank=True)
    unit_owner = models.CharField(
        max_length=3, null=True, blank=True, choices=UNIT_OWNERS)

    def __str__(self):
        return self.unit_type + '' + self.unit_number + '' + self.unit_owner
