from rest_framework import serializers
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", read_only=True)

    problem_title = serializers.CharField(
        source="problem.title",
        read_only=True
    )

    class Meta:
        model = Submission
        fields = [
            "id",
            "user",
            "username",
            "problem",
            "problem_title",
            "language",
            "code",
            "verdict",
            "runtime",
            "memory",
            "submitted_at",
        ]

        read_only_fields = [
            "user",
            "username",
            "problem_title",
            "verdict",
            "runtime",
            "memory",
            "submitted_at",
        ]

class SubmissionHistorySerializer(serializers.ModelSerializer):
    problem = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = [
            "id",
            "problem",
            "language",
            "verdict",
            "runtime",
            "memory",
            "submitted_at",
        ]

class SubmissionDetailSerializer(serializers.ModelSerializer):
    problem = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = [
            "id",
            "problem",
            "code",
            "language",
            "verdict",
            "runtime",
            "memory",
            "submitted_at",
        ]
from rest_framework import serializers


class RunCodeSerializer(serializers.Serializer):

    language = serializers.CharField(max_length=30)

    code = serializers.CharField()

    input_data = serializers.CharField()