from rest_framework import serializers 
# from django .contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
# User = get_user_model()
from .models import UserData
class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(Write_only=True)
    
    class Meta:
        model = UserData
        fields = ("id", "email", "username", "password")

        def create(self, validated_data):
            user = UserData.objects.create(email=validated_data["email"],name=validated_data["name"])
            user.set_password(validated_data["password"])
            user.save()
            return user

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "email", "username", "phone")