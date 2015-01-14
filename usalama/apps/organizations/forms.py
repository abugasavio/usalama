from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from .models import Organization


class SignupForm(forms.Form):
    organization = forms.CharField(label='Organization Name', required=True)
    email = forms.EmailField()
    phone_number = PhoneNumberField(label='Phone Number')
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def save(self):
        email = self.cleaned_data['email']
        user = User.objects.create_user(self.cleaned_data['username'], email, self.cleaned_data['password1'],)
        Organization.objects.create(name=self.cleaned_data['organization'], phone_number=self.cleaned_data['phone_number'], email=email, user=user)

    def clean_password2(self):
        if not 'password1' in self.cleaned_data:
            return None

        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Enter the same password as above, for verification.')

        return self.cleaned_data['password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('A user with that username already exists.')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('A user with that email already exists.')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            Organization.objects.get(phone_number=phone_number)
        except Organization.DoesNotExist:
            return phone_number
        raise forms.ValidationError('A user with that phone number already exists.')

    def clean_organization_name(self):
        organization_name = self.cleaned_data['organization_name']
        try:
            Organization.objects.get(name=organization_name)
        except Organization.DoesNotExist:
            return organization_name
        raise forms.ValidationError('An organization with that name already exists.')