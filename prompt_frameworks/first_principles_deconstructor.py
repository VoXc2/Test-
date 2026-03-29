"""Framework 8: First Principles Deconstructor - Fundamental Truth Analysis."""

from .base_framework import BaseFramework


class FirstPrinciplesDeconstructor(BaseFramework):
    name = "First Principles Deconstructor"
    name_ar = "مفكك المبادئ الأولى"
    description = "Break any problem down to fundamental truths and rebuild solutions from scratch"
    description_ar = "تفكيك أي مشكلة إلى حقائقها الأساسية وإعادة بناء الحلول من الصفر"

    def get_required_inputs(self) -> list:
        return ["problem_or_assumption"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.first_principles_deconstructor '<problem or assumption>'")
        sys.exit(1)

    fw = FirstPrinciplesDeconstructor()
    result = fw.run(problem_or_assumption=" ".join(sys.argv[1:]))
    print(result)
