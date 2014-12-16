from django.db import models
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from author.decorators import with_author


@with_author
class VehicleOwner(TimeStampedModel):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


@with_author
class Vehicle(TimeStampedModel):
    registration_number = models.CharField(max_length=20, blank=False)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    vehicle_owner = models.ForeignKey(VehicleOwner, related_name='registrationunit_vehicle')

    def __unicode__(self):
        return self.registration_number



