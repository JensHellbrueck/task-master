from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Configuration
from main.serializers.configuration import ConfigurationSerializer

class ConfigurationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
        
    filterset_fields = ["name"]
