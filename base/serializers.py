from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField()
    profile_picture = serializers.ImageField()
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=True)
    is_superuser = serializers.BooleanField(default=False)
    def create(self,validated_data): 
        return CustomUser.objects.create(**validated_data)
    def update(self,instance,validated_data):