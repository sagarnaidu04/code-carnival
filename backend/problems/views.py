from rest_framework import generics
from .models import Problem, TestCase
from .serializers import ProblemSerializer, TestCaseSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Boilerplate
from .serializers import BoilerplateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings
from pathlib import Path
from django.http import JsonResponse
from django.contrib.auth import get_user_model

def create_admin(request):
    User = get_user_model()

    if User.objects.filter(username="admin").exists():
        return JsonResponse({"message": "Admin already exists"})

    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="Admin@123"
    )

    return JsonResponse({"message": "Admin created successfully"})

def seed_database(request):
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin@123"
        )

    seed_file = Path(settings.BASE_DIR) / "seed_problems.py"
    exec(seed_file.read_text(encoding="utf-8"), {})

    return JsonResponse({"status": "success"})


class BoilerplateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        boilerplates = Boilerplate.objects.filter(problem_id=pk)
        serializer = BoilerplateSerializer(boilerplates, many=True)
        return Response(serializer.data)

class ProblemListCreateView(generics.ListCreateAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    pagination_class = None

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["difficulty"]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "title",
        "difficulty",
        "created_at",
    ]

    ordering = ["title"]
class ProblemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]

class TestCaseListCreateView(generics.ListCreateAPIView):

    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

    permission_classes = [IsAdminUser]


class TestCaseDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

    permission_classes = [IsAdminUser]