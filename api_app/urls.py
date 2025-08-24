from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    index,
    HarvestViewSet,
    PackageViewSet,
    InventoryViewSet,
    QualityControlViewSet,
    DispatchViewSet
)

router = DefaultRouter()
router.register(r'harvests', HarvestViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'quality-control', QualityControlViewSet)
router.register(r'dispatches', DispatchViewSet)

urlpatterns = [
    path('', index, name='index'),          
    path('api/', include(router.urls)),        
]
