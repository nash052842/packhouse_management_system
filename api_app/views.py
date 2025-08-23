from rest_framework import viewsets
from operations.models import Harvest, Package, Inventory, QualityControl, Dispatch
# from .serializers import HarvestSerializer, PackageSerializer, InventorySerializer, QualityControlSerializer, DispatchSerializer
from django.http import HttpResponse
from .serializers import HarvestSerializer, PackageSerializer, InventorySerializer, QualityControlSerializer, DispatchSerializer
from operations.models import Harvest, Package, Inventory, QualityControl, Dispatch

def index(request):
    return HttpResponse("Hello from api_app!")

class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class QualityControlViewSet(viewsets.ModelViewSet):
    queryset = QualityControl.objects.all()
    serializer_class = QualityControlSerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
