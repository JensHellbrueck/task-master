from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Milestone
from main.serializers.milestone import MilestoneSerializer


class MilestoneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    filterset_fields = ["project"]

    def get_queryset(self):
        return self.queryset.filter(project__owner=self.request.user)
