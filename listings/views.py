from rest_framework import viewsets,permissions
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Category,Property,PropertyImage
from .serializers import CategorySerializer,PropertySerializer,PropertyImageSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import PropertyFilter

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAdminUser]
    lookup_field= "slug"
class PropertyViewSet(viewsets.ModelViewSet):
    queryset=Property.objects.select_related("owner","category").prefetch_related("image")
    serializer_class=PropertySerializer
    permissions_class=[permissions,IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filterset_class=PropertyFilter
    search_fields=["title","city","address","description"]
    ordering_class=["price","created_at","area_sqm"]
    parser_classes=[MultiPartParser, FormParser]
    lookup_field="slug"
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset=PropertyImage.objects.select_related("property")
    serializer_class=PropertyImageSerializer
    permission_classes=[permissions.IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]
    def perform_create(self,serializer):
        # only owner and admin 
        prop =serializer.validated_data.get("property")
        user=self.request.user
        if (prop.owner_id !=user.id)and(not user.is_staff):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("you have not permission to upload this property")
        serializer.save()