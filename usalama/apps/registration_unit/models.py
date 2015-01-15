from django.db import models
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from author.decorators import with_author
from djchoices import DjangoChoices, ChoiceItem


@with_author
class VehicleMake(TimeStampedModel):
    name = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.name

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

    class ColorType(DjangoChoices):
        White = ChoiceItem('white', 'White')
        Silver = ChoiceItem('silver', 'Silver')
        Black = ChoiceItem('black', 'Black')
        Grey = ChoiceItem('grey', 'Grey')
        Blue = ChoiceItem('blue', 'Blue')
        Red = ChoiceItem('red', 'Red')
        Brown = ChoiceItem('brown', 'Brown')
        Green = ChoiceItem('green', 'Green')
        Other = ChoiceItem('other', 'Other')

    registration_number = models.CharField(max_length=20, blank=False)
    make = models.ForeignKey(VehicleMake, related_name='registrationunit_vehicle')
    model = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=ColorType.choices)
    vehicle_owner = models.ForeignKey(VehicleOwner, related_name='registrationunit_vehicle')

    def __unicode__(self):
        return self.registration_number



