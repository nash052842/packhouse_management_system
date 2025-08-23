        
from rest_framework import serializers
from . models import Harvest, Package,QualityControl, Harvest, Package, Inventory, Dispatch

class modelserializer(serializers.HarvestSerializer):
     class Meta:
        model= Harvest
        fields= '__all__'
class modelserializer(serializers.PackageSerializer):
     class Meta:
        model = Package
        fields = '__all__'

class modelserializer(serializers.QualityControlSerializer):
    class Meta:
        model = QualityControl
        fields = '__all__'

class modelserializer(serializers.InventorySerializer):
     class Meta:
        model = Inventory
        fields = '__all__'

class modelserializer(serializers.DispatchSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'

