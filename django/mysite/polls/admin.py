from django.contrib import admin
from .models import Vehicle, VehicleModel, VehicleCountry, VehicleBrand, VehicleType
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleModel)
admin.site.register(VehicleCountry)
admin.site.register(VehicleBrand)