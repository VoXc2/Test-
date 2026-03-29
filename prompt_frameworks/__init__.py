from .base_framework import BaseFramework
from .career_survival_scanner import CareerSurvivalScanner
from .constitutional_reasoning import ConstitutionalReasoning
from .industry_transformation import IndustryTransformationMap
from .deep_thinking_protocol import DeepThinkingProtocol
from .life_decision_framework import LifeDecisionFramework
from .opportunity_finder import OpportunityFinder

FRAMEWORKS = {
    "career_survival": CareerSurvivalScanner,
    "constitutional_reasoning": ConstitutionalReasoning,
    "industry_transformation": IndustryTransformationMap,
    "deep_thinking": DeepThinkingProtocol,
    "life_decision": LifeDecisionFramework,
    "opportunity_finder": OpportunityFinder,
}

__all__ = [
    "BaseFramework",
    "FRAMEWORKS",
    "CareerSurvivalScanner",
    "ConstitutionalReasoning",
    "IndustryTransformationMap",
    "DeepThinkingProtocol",
    "LifeDecisionFramework",
    "OpportunityFinder",
]
