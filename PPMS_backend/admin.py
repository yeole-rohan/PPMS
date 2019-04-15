from django.contrib import admin
from .models import DieselNozzle, DieselStock, Account

# Register your models here.
admin.site.register(Account)
admin.site.register(DieselStock)
admin.site.register(DieselNozzle)
