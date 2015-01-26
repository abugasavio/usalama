from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item('main', MenuItem('Vehicles',
                               reverse('registration_unit.vehicle_list'),
                               weight=1,
                               check=lambda request: request.user.has_perm('registration_unit.vehicle_list')
                               ))

Menu.add_item('main', MenuItem('Owners',
                               reverse('registration_unit.vehicleowner_list'),
                               weight=2,
                               check=lambda request: request.user.has_perm('registration_unit.vehicleowner_list')
                               ))