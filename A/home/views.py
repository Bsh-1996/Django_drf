from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Person, Question, Answer
from . serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
# Create your views here.


class Home(APIView):
   permission_classes = [IsAuthenticated, IsAdminUser]
   def get(self, request):
      person = Person.objects.all()
      ser_data = PersonSerializer(instance = person, many = True)
      return Response(data= ser_data.data)
   





class QuestionView(APIView):
   def get(self, request):
      questions = Question.objects.all()
      ser_data = QuestionSerializer(instance = questions, many = True).data
      return Response(ser_data, status=status.HTTP_200_OK)



   def post(self, request):
      pass 

   def put(self, request):
      pass 

   def delete(self, request):
      pass       
     