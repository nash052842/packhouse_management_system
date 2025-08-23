from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HarvestViewSet, PackageViewSet, InventoryViewSet, QualityControlViewSet, DispatchViewSet

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'harvests', HarvestViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'quality-control', QualityControlViewSet)
router.register(r'dispatches', DispatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
