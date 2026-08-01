from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContestProblem
from problems.serializers import ProblemSerializer

from .models import Contest, ContestRegistration

from .models import Contest
from .serializers import ContestSerializer
from django.db.models import Count, Q
from django.contrib.auth import get_user_model
from submissions.models import Submission

User = get_user_model()


class ContestListCreateView(generics.ListCreateAPIView):

    queryset = Contest.objects.all().order_by("-start_time")
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ContestRegisterView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        contest = Contest.objects.get(pk=pk)

        registration, created = ContestRegistration.objects.get_or_create(
            contest=contest,
            user=request.user
        )

        if not created:
            return Response(
                {"message": "Already registered"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Registration successful"},
            status=status.HTTP_201_CREATED
        )

class ContestProblemListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        contest = Contest.objects.get(pk=pk)

        problems = [
            cp.problem
            for cp in ContestProblem.objects.filter(contest=contest)
        ]

        serializer = ProblemSerializer(problems, many=True)

        return Response(serializer.data)
class ContestLeaderboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        contest = Contest.objects.get(pk=pk)

        problem_ids = ContestProblem.objects.filter(
            contest=contest
        ).values_list("problem_id", flat=True)

        leaderboard = User.objects.annotate(

            solved=Count(
                "submissions__problem",
                filter=Q(
                    submissions__problem__in=problem_ids,
                    submissions__verdict="Accepted",
                ),
                distinct=True,
            ),

            total_submissions=Count(
                "submissions",
                filter=Q(
                    submissions__problem__in=problem_ids
                ),
            ),

        ).order_by("-solved", "total_submissions", "username")

        data = []

        for rank, user in enumerate(leaderboard, start=1):

            data.append({
                "rank": rank,
                "username": user.username,
                "problems_solved": user.solved,
                "total_submissions": user.total_submissions,
            })

        return Response(data)