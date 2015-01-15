#from smartmin.users.models import *  # Required for smartmin user models to be generated and imported
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from author.decorators import with_author
from djchoices import DjangoChoices, ChoiceItem


@with_author
class Organization(TimeStampedModel):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    user = models.OneToOneField(User, related_name='organization')

    def __unicode__(self):
        return self.name


@with_author
class OrganizationVehicle(TimeStampedModel):
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
    make = models.ForeignKey('registration_unit.VehicleMake', related_name='OrganizationVehicle')
    model = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=ColorType.choices)
    organization = models.ForeignKey(Organization, related_name='organization_vehicle', null=False, blank=False)

    def __unicode__(self):
        return "{0}-{1}".format(self.registration_number, self.make)


@with_author
class OrganizationDriver(TimeStampedModel):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField()
    organization = models.ForeignKey(Organization, related_name='driver', null=False, blank=False)
