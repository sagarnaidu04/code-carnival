from django.urls import path
from .views import RunCodeView, SubmissionListCreateView
from .views import SubmissionHistoryView
from .views import SubmissionDetailView

urlpatterns = [
    path("", SubmissionListCreateView.as_view(), name="submission-list"),
    path("history/",SubmissionHistoryView.as_view(),name="submission-history"),
    path("<int:pk>/", SubmissionDetailView.as_view(), name="submission-detail"),
    path("run/",RunCodeView.as_view(),name="run-code"),
]