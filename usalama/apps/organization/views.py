from django.views.generic import FormView
from django.conf import settings
from django.contrib import messages
from django.utils.html import mark_safe
from django.shortcuts import redirect
from smartmin.views import SmartCRUDL, SmartCreateView, SmartListView
from .forms import SignupForm
from .models import OrganizationVehicle, OrganizationDriver


class Signup(FormView):
    form_class = SignupForm
    success_url = settings.LOGIN_URL
    template_name = 'organization_signup.html'

    @classmethod
    def derive_url_pattern(cls, path, action):
        return r'^signup/$'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, mark_safe("Your account has been created. Please login below to proceed."))
        return redirect(settings.LOGIN_URL)


class OrganizationVehicleCRUDL(SmartCRUDL):
    model = OrganizationVehicle
    actions = ('create', 'list', 'update',)
    permissions = True

    class Create(SmartCreateView):
        fields = ('registration_number', 'make', 'model', 'engine_number', 'color')

        def pre_save(self, obj):
            obj = super(OrganizationVehicleCRUDL.Create, self).pre_save(obj)
            obj.organization = self.request.user.profile.organization
            return obj

    class List(SmartListView):
        fields = ('registration_number', 'make', 'model', 'engine_number', 'color')


class OrganizationDriverCRUDL(SmartCRUDL):
    model = OrganizationDriver
    actions = ('create', 'list', 'update',)
    permissions = True

    class Create(SmartCreateView):
        fields = ('first_name', 'last_name', 'email', 'phone_number')

        def pre_save(self, obj):
            obj = super(OrganizationDriverCRUDL.Create, self).pre_save(obj)
            obj.organization = self.request.user.profile.organization
            return obj

    class List(SmartListView):
        fields = ('first_name', 'last_name', 'email', 'phone_number')


