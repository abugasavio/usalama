#from smartmin.users.models import *  # Required for smartmin user models to be generated and imported
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from author.decorators import with_author


@with_author
class Organization(TimeStampedModel):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    user = models.OneToOneField(User, related_name='organization')


@with_author
class OrganizationVehicle(TimeStampedModel):
    registration_number = models.CharField(max_length=20, blank=False)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    organization = models.ForeignKey(Organization, related_name='organization_vehicle', null=False, blank=False)


@with_author
class OrganizationDriver(TimeStampedModel):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField()
    organization = models.ForeignKey(Organization, related_name='driver', null=False, blank=False)
