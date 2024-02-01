from django.contrib import admin
from .models import Part
from .models import Vehicle
from .models import Fuel
from .models import Test

# Register your models here.
class PartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Part, PartAdmin)

class VehicleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vehicle, VehicleAdmin)

class FuelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fuel, FuelAdmin)

class TestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test, TestAdmin)