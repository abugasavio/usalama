from django.contrib import admin
from .models import Organization, OrganizationVehicle, OrganizationDriver, VehicleMake


class VehicleMakeAdmin(admin.ModelAdmin):
    pass


class OrganizationAdmin(admin.ModelAdmin):
    pass


class OrganizationVehicleAdmin(admin.ModelAdmin):
    pass


class OrganizationDriverAdmin(admin.ModelAdmin):
    pass

admin.site.register(VehicleMake, VehicleMakeAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationVehicle, OrganizationVehicleAdmin)
admin.site.register(OrganizationDriver, OrganizationDriverAdmin)