"""Framework 6: Opportunity Finder - Amodei 100-Year Acceleration.

Finds intersections of your skills with AI capabilities for unique
value creation. Identifies first-mover windows, proposes concrete
30-day experiments, and focuses on 10x transformation over 10% improvement.
"""

from .base_framework import BaseFramework


class OpportunityFinder(BaseFramework):
    name = "Opportunity Finder"
    name_ar = "مكتشف الفرص"
    description = "Find AI x Skills intersection opportunities using Amodei's acceleration thesis"
    description_ar = "اكتشف فرص تقاطع مهاراتك مع الذكاء الاصطناعي حسب أطروحة أمودي عن التسارع"

    def get_required_inputs(self) -> list:
        return ["position_description"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.opportunity_finder '<your position>'")
        sys.exit(1)

    finder = OpportunityFinder()
    result = finder.run(position_description=" ".join(sys.argv[1:]))
    print(result)
