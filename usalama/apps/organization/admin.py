from django.contrib import admin
from .models import Organization, OrganizationVehicle, OrganizationDriver


class OrganizationAdmin(admin.ModelAdmin):
    pass


class OrganizationVehicleAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'make', 'model', 'engine_number', 'color')


class OrganizationDriverAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationVehicle, OrganizationVehicleAdmin)
admin.site.register(OrganizationDriver, OrganizationDriverAdmin)