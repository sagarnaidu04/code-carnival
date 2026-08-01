from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Submission
from .serializers import SubmissionDetailSerializer, SubmissionSerializer
from .judge import JudgeService
from .serializers import SubmissionHistorySerializer
from rest_framework import generics
from .serializers import RunCodeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RunCodeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = RunCodeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        result = JudgeService.execute(

            code=serializer.validated_data["code"],

            language=serializer.validated_data["language"],

            stdin=serializer.validated_data["input_data"],
        )

        return Response(result)

class SubmissionDetailView(generics.RetrieveAPIView):

    serializer_class = SubmissionDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)


class SubmissionListCreateView(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)


    def perform_create(self, serializer):

        submission = serializer.save(user=self.request.user)

        JudgeService.judge(submission)

class SubmissionHistoryView(generics.ListAPIView):

    serializer_class = SubmissionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Submission.objects
            .filter(user=self.request.user)
            .order_by("-submitted_at")
        )