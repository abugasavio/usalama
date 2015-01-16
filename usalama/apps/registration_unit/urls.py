from .views import VehicleCRUDL, VehicleOwnerCRUDL

urlpatterns = VehicleCRUDL().as_urlpatterns()
urlpatterns += VehicleOwnerCRUDL().as_urlpatterns()