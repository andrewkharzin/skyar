from django.db import models

# Create your models here.


class Flight(models.Model):
    AC_TYPE = (
        ('B737', 'B737'),
        ('B747', 'B747'),
        ('A330', 'A330'),
        ('B777', 'B777'),

    )
    f_type = models.CharField(null=True, blank=True,
                              max_length=10, choices=AC_TYPE)
    f_number = models.CharField(
        null=True, blank=True, max_length=6, default='')
    f_registration = models.CharField(
        null=True, blank=True, max_length=5, default='')

    def __str__(self):
        return self.f_number + '-' + self.f_registration
# class Schedule(models.Model):
