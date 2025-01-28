from .models import CustomUser,Book,Category,Author
from .serializers import CustomUserSerializer,BookSerializer,CategorySerializer,AuthorSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CustomUserViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = CustomUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = CustomUserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class BookViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = BookSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = BookSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response({"detail": "book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class AuthorViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = AuthorSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = AuthorSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = AuthorSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response({"detail": "Author deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class CategorySerializer(viewsets.ViewSet):
    def create(self,request):
        serializer = CategorySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = CategorySerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = CategorySerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response({"detail": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    