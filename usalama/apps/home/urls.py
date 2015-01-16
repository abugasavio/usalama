from django.conf.urls import url, patterns
from .views import HomeRedirectView

urlpatterns = patterns('',
                       url(r'^$', HomeRedirectView.as_view(), name='home.homeredirect'),
                       )
