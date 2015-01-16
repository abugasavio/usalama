from django.views.generic import RedirectView
from django.conf import settings
from django.core.urlresolvers import reverse


class HomeRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if settings.GROUP_REG_UNIT in self.request.user.groups.all():
            return reverse('registration_unit.vehicle_list')
        else:
            return reverse('organizations.organizationvehicle_list')