from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/accounts/", include("accounts.urls")),

    path("api/problems/", include("problems.urls")),

    path("api/submissions/", include("submissions.urls")),

    path("api/contests/", include("contests.urls")),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    path("api/", include("core.urls")),
]