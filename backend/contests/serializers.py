from rest_framework import serializers
from .models import Contest, ContestProblem, ContestRegistration


class ContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contest
        fields = "__all__"
        read_only_fields = ["created_by"]


class ContestProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContestProblem
        fields = "__all__"


class ContestRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContestRegistration
        fields = "__all__"
        read_only_fields = ["user", "registered_at"]