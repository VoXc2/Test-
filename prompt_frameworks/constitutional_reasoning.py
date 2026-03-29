"""Framework 2: Constitutional Reasoning Engine - Anthropic Style.

Evaluates answers against core principles: helpful, honest, complete,
and serving long-term interests. Includes confidence scoring and
counter-arguments.
"""

from .base_framework import BaseFramework


class ConstitutionalReasoning(BaseFramework):
    name = "Constitutional Reasoning Engine"
    name_ar = "محرك الاستدلال الدستوري"
    description = "AI that evaluates every answer against Anthropic's constitutional principles"
    description_ar = "ذكاء اصطناعي يقيّم كل جواب حسب مبادئ أنثروبيك الدستورية"

    def get_required_inputs(self) -> list:
        return ["question"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.constitutional_reasoning '<your question>'")
        sys.exit(1)

    engine = ConstitutionalReasoning()
    result = engine.run(question=" ".join(sys.argv[1:]))
    print(result)
