from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Problem, TestCase, Boilerplate
from .serializers import (
    ProblemSerializer,
    TestCaseSerializer,
    BoilerplateSerializer,
)



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