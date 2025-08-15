from django import dispatch
from rest_framework import serializers
from . models import Harvest, Package, Quality_control, harvest,package,quality_control,inventory,distpach

class modelserilaizer(serializers.HarvetsSerializer):
     class Meta:
        model= Harvest
        fields= '__all__'
class modelserializer(serializers.PackageSerializer):
     class Meta:
        models = Package
        fields = '__all__'

class modelserializer(serializers.Quality_controlSerializer):
    class Meta:
        model = Quality_control
        fields = '__all__'

class modelserializer(serializers.InventorySerilizer):
     class Meta:
        model = inventory
        fields = '__all__'

class modelserializer(serializers.DispatchSerilizer):
    class Meta:
        model =dispatch
        fields = '__all__'

