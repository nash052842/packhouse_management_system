from rest_framework import viewsets
from. import harvest, package,inventory,quality_control,dispatch
from serializers import harvestserializers,packageserializers,quality_controlserilaizers,inventoryserilizers,distpachserilizers

class HarvestViewset(viewsets.ModelViewSet):
    queryset = harvest .objects.all()
    serializer_class = harvestserializers

class PackageViewset(viewsets.ModelViewSet):
    queryset = package.objecst.all()
    serializer_class = packageserializers

class Quality_controlViewset(viewsets.ModelViewSet):
    queryset = quality_control.objects.all()
    serializer_class = quality_controlserilaizers

class InventoryViewset(viewsets.ModelViewSet):
    queryset = inventory.objects.all()
    serializer_class = inventoryserilizers

class dispatchViewset(viewsets.ModelViewSet):
    queryset = dispatch.objects.all()
    serializer_class = distpachserilizers
