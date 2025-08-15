
from django.contrib import admin
from .models import Inventory, Quality_control, Harvest,Package,Distpach

admin.site.register(Inventory)
admin.site.register(Harvest)
admin.site.register(Quality_control)
admin.site.register(Package)
admin.site.register (Distpach)
