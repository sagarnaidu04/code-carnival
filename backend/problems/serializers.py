from rest_framework import serializers
from .models import Boilerplate, Problem,TestCase


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = "__all__"

class TestCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCase
        fields = "__all__"

class BoilerplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boilerplate
        fields = "__all__"