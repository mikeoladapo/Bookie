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

    