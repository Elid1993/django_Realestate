from django.urls import path ,include
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet,PropertyViewSet,PropertyImageViewSet

router=SimpleRouter()
router.register("categories",CategoryViewSet,basename="category")
router.register("properties",PropertyViewSet,basename="property")
router.register("images",PropertyImageViewSet,basename="prop-image")

urlpatterns = [
    path ("",include(router.urls)),
    ]
