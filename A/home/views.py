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
      ser_data = QuestionSerializer(data = request.POST)
      if ser_data.is_valid():
         ser_data.save()
         return Response(ser_data.data, status=status.HTTP_201_CREATED)
      return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
   


   def put(self, request, pk):
      question = Question.objects.get(id=pk)
      ser_data = QuestionSerializer(instance= question, data=request.POST, partial = True)
      if ser_data.is_valid():
         ser_data.save()
         return Response(ser_data.data, status=status.HTTP_200_OK)
      return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
         



   def delete(self, request, pk):
      question = Question.objects.get(id= pk)
      question.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   
   
     