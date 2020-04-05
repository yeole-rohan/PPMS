from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import DieselNozzle, DieselStock, Account,DieselDensity,PetrolDensity,PetrolNozzle,PetrolStock

# Register your models here.
admin.site.register(Account)
admin.site.register(DieselStock)
admin.site.register(DieselNozzle)
admin.site.register(DieselDensity)
admin.site.register(PetrolDensity)
admin.site.register(PetrolNozzle)
admin.site.register(PetrolStock)
