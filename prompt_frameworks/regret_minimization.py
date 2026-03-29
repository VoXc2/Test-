"""Framework 12: Regret Minimization Framework - Bezos-style long-term decision making.

Helps users make bold, long-term decisions by projecting themselves to age 80
and asking which choice they would regret NOT making.
"""

from .base_framework import BaseFramework


class RegretMinimization(BaseFramework):
    name = "Regret Minimization Framework"
    name_ar = "إطار تقليل الندم"
    description = "Bezos-style regret minimization - project yourself to age 80 and decide"
    description_ar = "إطار تقليل الندم على طريقة بيزوس — تخيل نفسك في سن الثمانين واتخذ القرار"

    def get_required_inputs(self) -> list:
        return ["life_choice"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.regret_minimization '<life choice>'")
        sys.exit(1)

    fw = RegretMinimization()
    result = fw.run(life_choice=" ".join(sys.argv[1:]))
    print(result)
