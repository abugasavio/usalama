from django.utils.safestring import mark_safe
from smartmin.views import SmartCRUDL, SmartCreateView, SmartListView
from .models import Vehicle, VehicleOwner


class VehicleCRUDL(SmartCRUDL):
    model = Vehicle
    actions = ('create', 'list', )

    class Create(SmartCreateView):
        fields = ('registration_number', 'make', 'model', 'engine_number', 'color', 'vehicle_owner')
        field_config = {
            'vehicle_owner': dict(help=mark_safe('If vehicle owner does not exist, <a href="/registration-unit/vehicleowner/create/">click here</a> to add new owner')),
        }

    class List(SmartListView):
        fields = ('registration_number', 'make', 'model', 'engine_number', 'color', 'vehicle_owner')
        link_fields = ('registration_number', 'engine_number')


class VehicleOwnerCRUDL(SmartCRUDL):
    model = VehicleOwner

    class List(SmartListView):
        fields = ('first_name', 'last_name', 'email', 'phone_number')
        link_fields = ('email', 'first_name')

