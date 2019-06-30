from .models import Task  # Import Task model
from .serializers import TaskSerializer  # Import the serializer

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()  # Select all tasks
    serializer_class = TaskSerializer  # Serialize data
