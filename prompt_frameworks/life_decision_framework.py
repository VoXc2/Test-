"""Framework 5: Life Decision Framework - Anthropic HHH Style.

Applies Helpful, Harmless, Honest principles to major life decisions.
Analyzes what you want to hear vs what you need to hear, trade-offs,
long-term consequences, and the uncomfortable truth you're avoiding.
"""

from .base_framework import BaseFramework


class LifeDecisionFramework(BaseFramework):
    name = "Life Decision Framework"
    name_ar = "إطار قرار الحياة"
    description = "Analyze life decisions using Anthropic's HHH principles"
    description_ar = "تحليل قرارات الحياة الكبيرة باستخدام مبادئ أنثروبيك: مفيد، غير ضار، صادق"

    def get_required_inputs(self) -> list:
        return ["decision"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.life_decision_framework '<your decision>'")
        sys.exit(1)

    framework = LifeDecisionFramework()
    result = framework.run(decision=" ".join(sys.argv[1:]))
    print(result)
