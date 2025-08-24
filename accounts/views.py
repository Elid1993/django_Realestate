from rest_framework import generics
from .serializers import UserSerializer
from .models import UserData
class RegisterView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class= UserSerializer
#     permission_classes=[permissions.AllowAny]
    
# class MeView(generics.RetrieveAPIView):
#     serializer_class= UserSerializer 
#     permission_classes=[permissions.IsAuthenticated]
    
#     def get_object(self):
#         return self.request.user
