from django.apps import AppConfig


class ProblemsConfig(AppConfig):
    name = "problems"

    def ready(self):
        import os

        # Prevent running twice because of Django autoreload
        if os.environ.get("RUN_MAIN") == "true":
            return

        try:
            from .models import Problem

            # Only seed when production DB is empty
            if Problem.objects.count() == 0:
                from pathlib import Path
                from django.conf import settings

                seed_file = Path(settings.BASE_DIR) / "seed_problems.py"

                if seed_file.exists():
                    print("🌱 Seeding problems...")
                    exec(seed_file.read_text(encoding="utf-8"), {})
                    print("✅ Problems imported.")

        except Exception as e:
            print("Seed skipped:", e)