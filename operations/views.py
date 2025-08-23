from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import render
from .models import Harvest, Package, Inventory, QualityControl, Dispatch
from .serializers import (
    HarvestSerializer,
    PackageSerializer,
    QualityControlSerializer,
    InventorySerializer,
    DispatchSerializer
)

class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class QualityControlViewSet(viewsets.ModelViewSet):
    queryset = QualityControl.objects.all()
    serializer_class = QualityControlSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
