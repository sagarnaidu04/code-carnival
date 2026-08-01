from django.urls import path
from .views import ContestListCreateView
from .views import ContestListCreateView, ContestRegisterView
from .views import ContestListCreateView,ContestRegisterView,ContestProblemListView
from .views import ContestLeaderboardView

urlpatterns = [
    path("", ContestListCreateView.as_view(), name="contest-list"),
    path("<int:pk>/register/", ContestRegisterView.as_view(), name="contest-register"),
    path("<int:pk>/problems/",ContestProblemListView.as_view(),name="contest-problems"),
    path("<int:pk>/leaderboard/", ContestLeaderboardView.as_view(), name="contest-leaderboard"),
]
