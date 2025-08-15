from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from Operations.views import HarvestViewSet, PackageViewSet, QualityControlViewSet, InventoryViewSet, DispatchViewSet

router = DefaultRouter()
router.register(r"harvest", HarvestViewSet)
router.register(r"package", PackageViewSet)
router.register(r"inventory", InventoryViewSet)
router.register(r"quality_control", QualityControlViewSet)
router.register(r"dispatch", DispatchViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
