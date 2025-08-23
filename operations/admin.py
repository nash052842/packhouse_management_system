
from django.contrib import admin
from .models import Inventory, QualityControl, Harvest, Package, Dispatch

admin.site.register(Inventory)
admin.site.register(Harvest)
admin.site.register(QualityControl)
admin.site.register(Package)
admin.site.register(Dispatch)
