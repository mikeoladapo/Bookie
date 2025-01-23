from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=True)
    is_superuser = serializers.BooleanField(default=False)
    def create(self,validated_data):