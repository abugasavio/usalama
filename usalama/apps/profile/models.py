from django.db import models
from django.contrib.auth.models import User
#from smartmin.users.models import *  # Required for smartmin user models to be generated and imported
from django_extensions.db.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile')
    organization = models.ForeignKey('organization.Organization', related_name='user_profile', null=False, blank=False)