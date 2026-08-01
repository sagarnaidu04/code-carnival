from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problem

User = get_user_model()


class Submission(models.Model):

    LANGUAGES = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("C++", "C++"),
    )

    VERDICTS = (
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Wrong Answer", "Wrong Answer"),
        ("Runtime Error", "Runtime Error"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    language = models.CharField(max_length=20, choices=LANGUAGES)

    code = models.TextField()

    verdict = models.CharField(
        max_length=30,
        choices=VERDICTS,
        default="Pending",
    )

    runtime = models.FloatField(default=0)

    memory = models.IntegerField(default=0)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"