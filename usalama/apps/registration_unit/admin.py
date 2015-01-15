from django.contrib import admin
from .models import VehicleMake


class VehicleMakeAdmin(admin.ModelAdmin):
    pass


admin.site.register(VehicleMake, VehicleMakeAdmin)