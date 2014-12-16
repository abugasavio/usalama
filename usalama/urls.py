from django.conf.urls import patterns, include, url
from usalama.apps.organizations.views import Signup
from django.contrib import admin
# admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # admin:
                       url(r'^admin/', include(admin.site.urls)),
                       # .. other patterns ..
                       url(r'^users/', include('smartmin.users.urls')),
                       url(r'registration-unit/', include('usalama.apps.registration_unit.urls')),
                       url(r'organization/', include('usalama.apps.organizations.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'signup/$', Signup.as_view(), name='users.organization_signup'),
                       )
