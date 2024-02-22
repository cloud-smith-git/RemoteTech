from django.contrib import admin
from .models import PartRequest
from .models import VehicleCheck
from .models import FuelPurchase

class PartRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(PartRequest, PartRequestAdmin)

class VehicleCheckAdmin(admin.ModelAdmin):
    pass

admin.site.register(VehicleCheck, VehicleCheckAdmin)

class FuelPurchaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(FuelPurchase, FuelPurchaseAdmin)

