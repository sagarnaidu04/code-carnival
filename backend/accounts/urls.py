from django.urls import path
from .views import RegisterView, ProfileView
from .views import DashboardView,LeaderboardView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("dashboard/",DashboardView.as_view(),name="dashboard"),
    path("leaderboard/",LeaderboardView.as_view(),name="leaderboard"),
]