from rest_framework import viewsets, permissions
from auth_001.models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer