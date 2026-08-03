from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings
from pathlib import Path

User = get_user_model()


def seed_database(request):
    # Create admin if not exists
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin@123"
        )

    # Run your seed file
    seed_file = Path(settings.BASE_DIR) / "seed_problems.py"

    exec(seed_file.read_text(encoding="utf-8"), {})

    return JsonResponse({
        "status": "success",
        "message": "Database seeded successfully"
    })