from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Project
from main.serializers.project import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)