from django.urls import path
from .views import ProblemListCreateView,ProblemDetailView,TestCaseListCreateView,TestCaseDetailView
from .views import BoilerplateListView

urlpatterns = [
    path("", ProblemListCreateView.as_view(), name="problem-list"),
    path("<int:pk>/", ProblemDetailView.as_view(), name="problem-detail"),
    path("testcases/", TestCaseListCreateView.as_view()),
    path("testcases/<int:pk>/", TestCaseDetailView.as_view()),
    path(
        "<int:pk>/boilerplates/",
        BoilerplateListView.as_view(),
        name="problem-boilerplates",
    ),
]