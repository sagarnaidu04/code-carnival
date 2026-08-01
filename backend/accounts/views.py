from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, ProfileSerializer
from submissions.models import Submission

User = get_user_model()


# Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# User Profile
class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


# Dashboard
class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        submissions = Submission.objects.filter(user=user)

        total_submissions = submissions.count()

        accepted = submissions.filter(
            verdict="Accepted"
        ).count()

        wrong_answer = submissions.filter(
            verdict="Wrong Answer"
        ).count()

        runtime_error = submissions.filter(
            verdict="Runtime Error"
        ).count()

        problems_solved = (
            submissions.filter(verdict="Accepted")
            .values("problem")
            .distinct()
            .count()
        )

        acceptance_rate = (
            accepted / total_submissions * 100
            if total_submissions
            else 0
        )

        return Response({

            "username": user.username,

            "problems_solved": problems_solved,

            "total_submissions": total_submissions,

            "accepted": accepted,

            "wrong_answer": wrong_answer,

            "runtime_error": runtime_error,

            "acceptance_rate": round(acceptance_rate, 2),

        })
# Leaderboard
class LeaderboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        leaderboard = User.objects.annotate(

            problems_solved=Count(
                "submissions__problem",
                filter=Q(submissions__verdict="Accepted"),
                distinct=True,
            ),

            total_submissions=Count("submissions"),

        ).order_by("-problems_solved", "username")

        data = []

        for rank, user in enumerate(leaderboard, start=1):

            acceptance_rate = (
                user.problems_solved / user.total_submissions * 100
                if user.total_submissions else 0
            )

            data.append({
                "rank": rank,
                "username": user.username,
                "problems_solved": user.problems_solved,
                "total_submissions": user.total_submissions,
                "acceptance_rate": round(acceptance_rate, 2),
            })

        return Response(data)