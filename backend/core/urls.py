from django.urls import path
from .views import seed_database

urlpatterns = [
    path("seed/", seed_database),
]