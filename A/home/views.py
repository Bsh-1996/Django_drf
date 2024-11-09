from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Person
from . serializers import PersonSerializer
# Create your views here.



class Home(APIView):
   def get(self, request):
      person = Person.objects.get(name= 'ali hasani')
      ser_data = PersonSerializer(person)
      return Response(data= ser_data.data)
   
   
          
     