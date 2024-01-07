from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Task
from main.serializers.task import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ["milestone"]

    def get_queryset(self):
        return self.queryset.filter(
            milestone__project__owner=self.request.user
        )