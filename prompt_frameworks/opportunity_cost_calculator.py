"""Framework 14: Opportunity Cost Calculator - Calculate the true cost of any choice."""

from .base_framework import BaseFramework


class OpportunityCostCalculator(BaseFramework):
    name = "Opportunity Cost Calculator"
    name_ar = "حاسبة تكلفة الفرصة البديلة"
    description = "Calculate the true cost of any choice by analyzing what you give up"
    description_ar = "احسب التكلفة الحقيقية لأي خيار من خلال تحليل ما تتنازل عنه"

    def get_required_inputs(self) -> list:
        return ["options_description"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.opportunity_cost_calculator '<options description>'")
        sys.exit(1)

    fw = OpportunityCostCalculator()
    result = fw.run(options_description=" ".join(sys.argv[1:]))
    print(result)
