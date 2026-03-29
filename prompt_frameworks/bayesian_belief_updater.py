"""Framework 11: Bayesian Belief Updater - Rational belief updating with Bayesian reasoning.

Helps users update their beliefs rationally when new evidence arrives,
using formal Bayesian logic to overcome confirmation bias and availability bias.
"""

from .base_framework import BaseFramework


class BayesianBeliefUpdater(BaseFramework):
    name = "Bayesian Belief Updater"
    name_ar = "محدث المعتقدات البايزي"
    description = "Update your beliefs rationally when new evidence arrives using Bayesian reasoning"
    description_ar = "حدّث معتقداتك بعقلانية عند وصول أدلة جديدة باستخدام الاستدلال البايزي"

    def get_required_inputs(self) -> list:
        return ["belief_and_evidence"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m prompt_frameworks.bayesian_belief_updater '<belief and evidence>'")
        sys.exit(1)

    fw = BayesianBeliefUpdater()
    result = fw.run(belief_and_evidence=" ".join(sys.argv[1:]))
    print(result)
