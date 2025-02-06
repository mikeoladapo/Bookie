from rest_framework import serializers
from .models import CustomUser , Author ,Book ,Category
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

username_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9_]+$',
    message="Username must be alphanumeric or contain underscores."
)

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=20,
        validators=[username_regex],  
        error_messages={"unique": "username is already taken"}
    )
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField(required=False,allow_null=True)
    is_active = serializers.BooleanField(default=True,read_only=True)
    is_staff = serializers.BooleanField(default=True,read_only=True)
    is_superuser = serializers.BooleanField(default=False,read_only=True)
    def create(self,validated_data): 
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        return CustomUser.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.username = validated_data.get("username",instance.username)
        instance.email = validated_data.get("email",instance.email)
        password = validated_data.get("password")
        if password:
            instance.password = make_password(password)
        instance.profile_picture = validated_data.get("profile_picture",instance.profile_picture)
        instance.save()
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Author
        fields =  ['id', 'user', 'bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name','author','category','released_date','price','picture']
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.price = validated_data.get('price', instance.price)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance 
