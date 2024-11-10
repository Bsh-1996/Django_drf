from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Person
from . serializers import PersonSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.



class Home(APIView):
   permission_classes = [IsAuthenticated, IsAdminUser]

   def get(self, request):
      person = Person.objects.all()
      ser_data = PersonSerializer(person, many = True)
      return Response(data= ser_data.data)
   
   
          
     