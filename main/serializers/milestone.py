from rest_framework import serializers

from main.models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = "__all__"