from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create or update production admin"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        user, created = User.objects.get_or_create(
            username="admin",
            defaults={"email": "admin@example.com"},
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password("Admin@123")
        user.save()

        self.stdout.write(self.style.SUCCESS("Admin account is ready"))