"""Framework 10: Inversion Problem Solver - Inverse Failure Analysis."""

from .base_framework import BaseFramework


class InversionSolver(BaseFramework):
    name = "Inversion Problem Solver"
    name_ar = "حل المشكلات بالعكس"
    description = "Solve problems by inverting them - figure out how to guarantee failure, then avoid it"
    description_ar = "حل المشكلات عن طريق عكسها — اكتشف كيف تضمن الفشل ثم تجنبه"

    def get_required_inputs(self) -> list:
        return ["goal"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.inversion_solver '<goal>'")
        sys.exit(1)

    fw = InversionSolver()
    result = fw.run(goal=" ".join(sys.argv[1:]))
    print(result)
