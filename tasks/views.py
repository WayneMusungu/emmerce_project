from django.shortcuts import render
from django.http import JsonResponse

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TodoList(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return JsonResponse({'todo':serializer.data})
    
    
class TodoCreate(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class TodoDetail(APIView):
    def get(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer  = TodoSerializer(todo)
            return Response(serializer.data)
        
        
class TodoUpdate(APIView):
    def put(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'PUT':
            serializer = TodoSerializer(instance=todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TodoDelete(APIView):
    def delete(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            todo.delete()
            return Response('Your Todo Item has been deleted successfully!!')