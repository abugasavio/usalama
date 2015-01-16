from .views import OrganizationVehicleCRUDL, OrganizationDriverCRUDL

urlpatterns = OrganizationVehicleCRUDL().as_urlpatterns()
urlpatterns += OrganizationDriverCRUDL().as_urlpatterns()