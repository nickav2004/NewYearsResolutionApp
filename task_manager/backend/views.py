from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime

past_time = datetime.now()

def update_new_day():
    global past_time
    current_time = datetime.now()
    
    if(current_time.day > past_time.day):
        Task.objects.update(completed=False)
        past_time = datetime.now()
    

class GetTasks(APIView):
    def get(self, request, format=None):
        update_new_day()

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class AddTask(APIView):
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class FinishedTask(APIView):
    def put(self, request, id, format=None):
        try:
            task = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.completed = True
        task.save()
        
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteTask(APIView):
    def delete(self, request, id, format=None):
        try:
            task = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
        