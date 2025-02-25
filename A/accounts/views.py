from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from . serializers import UserRegisterSerializer, UserSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(instance = self.queryset, many = True)
        return Response(data=srz_data.data)

class UserApi(APIView):
    def get(self, request):
        queryset = User.objects.all()
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 2)
        paginator = Paginator(queryset, page_size,)
        srz_data = UserSerializer(instance = paginator.page(page_number), many = True)
        return Response(data=srz_data.data)

class UserListApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer










class UserRegister(APIView):
    def post(self, request):
        srz_data =  UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status= status.HTTP_400_BAD_REQUEST)
    


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(instance=self.queryset, many = True) 
        return Response(data=srz_data.data)
       
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk = pk)
        srz_data = UserSerializer(instance = user)
        return Response(data=srz_data.data)
    


    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk = pk)
        if user != request.user:
            return Response({'permission denied': 'you are noot the owner'})
        srz_data = UserSerializer(instance = user, data = request.POST, partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)
    

    def destroy(self, request, pk=None):
        if user != request.user:
            return Response({'permission denied': 'you are noot the owner'})
        user = get_object_or_404(self.queryset, pk = pk)
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated'})
