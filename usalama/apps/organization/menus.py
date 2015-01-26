from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item('main', MenuItem('Organization Vehicles',
                               reverse('organization.organizationvehicle_list'),
                               weight=3,
                               check=lambda request: request.user.has_perm('organization.organizationvehicle_list')
                               ))

Menu.add_item('main', MenuItem('Organization Drivers',
                               reverse('organization.organizationdriver_list'),
                               weight=4,
                               check=lambda request: request.user.has_perm('organization.organizationdriver_list')
                               ))
