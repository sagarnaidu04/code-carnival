from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problem

User = get_user_model()


class Contest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_contests"
    )

    def __str__(self):
        return self.title


class ContestProblem(models.Model):
    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name="contest_problems"
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("contest", "problem")


class ContestRegistration(models.Model):
    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contest_registrations"
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("contest", "user")