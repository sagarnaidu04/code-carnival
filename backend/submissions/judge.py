import requests
from django.conf import settings
from problems.models import TestCase


class JudgeService:

    @staticmethod
    def execute(code, language, stdin=""):
        payload = {
            "source_code": code,
            "language_id": settings.LANGUAGE_IDS[language.lower()],
            "stdin": stdin,
        }

        response = requests.post(
            f"{settings.JUDGE0_URL}/submissions/?wait=true",
            json=payload,
        )

        return response.json()

    @staticmethod
    def judge(submission):

        test_cases = TestCase.objects.filter(problem=submission.problem)

        verdict = "Accepted"
        runtime = 0
        memory = 0

        for tc in test_cases:

            result = JudgeService.execute(
                code=submission.code,
                language=submission.language,
                stdin=tc.input_data,
            )

            # If Judge0 reports an error
            if result.get("stdout") is None:
                verdict = "Runtime Error"
                break

            output = result["stdout"].strip()
            expected = tc.expected_output.strip()

            if output != expected:
                verdict = "Wrong Answer"
                break

            runtime = max(runtime, float(result.get("time") or 0))
            memory = max(memory, int(result.get("memory") or 0))

        submission.verdict = verdict
        submission.runtime = runtime
        submission.memory = memory

        submission.save()

        return submission