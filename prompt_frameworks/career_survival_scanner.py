"""Framework 1: Career Survival Scanner - Amodei Style.

Analyzes job exposure to AI disruption, classifies tasks as
AI-REPLACEABLE / AI-AUGMENTED / HUMAN-ESSENTIAL, and provides
a survival strategy with timeline.
"""

from .base_framework import BaseFramework


class CareerSurvivalScanner(BaseFramework):
    name = "Career Survival Scanner"
    name_ar = "ماسح بقاء المهنة"
    description = "Analyze your career's AI disruption risk using Amodei's framework"
    description_ar = "تحليل مخاطر اضطراب الذكاء الاصطناعي على مسارك المهني على طريقة أمودي"

    def get_required_inputs(self) -> list:
        return ["career_description"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.career_survival_scanner '<career description>'")
        print("Example: python -m prompt_frameworks.career_survival_scanner 'مهندس برمجيات، 5 سنوات خبرة، أعمل في تطوير تطبيقات الويب'")
        sys.exit(1)

    scanner = CareerSurvivalScanner()
    result = scanner.run(career_description=" ".join(sys.argv[1:]))
    print(result)
