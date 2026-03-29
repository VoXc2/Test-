"""Framework 3: Industry Transformation Map - Machines of Loving Grace.

Maps industry disruption across 3 waves (1-2yr, 3-5yr, 5-10yr),
identifies winners/losers, new roles, and provides a 90-day action plan.
"""

from .base_framework import BaseFramework


class IndustryTransformationMap(BaseFramework):
    name = "Industry Transformation Map"
    name_ar = "خريطة تحول الصناعة"
    description = "Map your industry's AI transformation across 3 waves"
    description_ar = "خريطة تحول صناعتك عبر 3 موجات من اضطراب الذكاء الاصطناعي"

    def get_required_inputs(self) -> list:
        return ["industry_description"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.industry_transformation '<industry description>'")
        sys.exit(1)

    mapper = IndustryTransformationMap()
    result = mapper.run(industry_description=" ".join(sys.argv[1:]))
    print(result)
