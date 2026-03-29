"""Framework 9: Second Order Thinking Engine - Cascading Consequences Analysis."""

from .base_framework import BaseFramework


class SecondOrderThinking(BaseFramework):
    name = "Second Order Thinking Engine"
    name_ar = "محرك التفكير من الدرجة الثانية"
    description = "Map cascading consequences of decisions through multiple orders of effects"
    description_ar = "رسم خريطة العواقب المتتالية للقرارات عبر مستويات متعددة من التأثيرات"

    def get_required_inputs(self) -> list:
        return ["proposed_action"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.second_order_thinking '<proposed action>'")
        sys.exit(1)

    fw = SecondOrderThinking()
    result = fw.run(proposed_action=" ".join(sys.argv[1:]))
    print(result)
