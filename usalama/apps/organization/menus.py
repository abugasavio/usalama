from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item('main', MenuItem('Organization Vehicles',
                               reverse('organization.organizationvehicle_list'),
                               weight=10,
                               ))

Menu.add_item('main', MenuItem('Organization Drivers',
                               reverse('organization.organizationdriver_list'),
                               weight=20,
                               ))
