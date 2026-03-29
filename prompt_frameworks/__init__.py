from .base_framework import BaseFramework
from .career_survival_scanner import CareerSurvivalScanner
from .constitutional_reasoning import ConstitutionalReasoning
from .industry_transformation import IndustryTransformationMap
from .deep_thinking_protocol import DeepThinkingProtocol
from .life_decision_framework import LifeDecisionFramework
from .opportunity_finder import OpportunityFinder
from .nash_equilibrium_strategist import NashEquilibriumStrategist
from .first_principles_deconstructor import FirstPrinciplesDeconstructor
from .second_order_thinking import SecondOrderThinking
from .inversion_solver import InversionSolver
from .bayesian_belief_updater import BayesianBeliefUpdater
from .regret_minimization import RegretMinimization
from .stakeholder_power_mapper import StakeholderPowerMapper
from .opportunity_cost_calculator import OpportunityCostCalculator

FRAMEWORKS = {
    "career_survival": CareerSurvivalScanner,
    "constitutional_reasoning": ConstitutionalReasoning,
    "industry_transformation": IndustryTransformationMap,
    "deep_thinking": DeepThinkingProtocol,
    "life_decision": LifeDecisionFramework,
    "opportunity_finder": OpportunityFinder,
    "nash_equilibrium": NashEquilibriumStrategist,
    "first_principles": FirstPrinciplesDeconstructor,
    "second_order_thinking": SecondOrderThinking,
    "inversion_solver": InversionSolver,
    "bayesian_updater": BayesianBeliefUpdater,
    "regret_minimization": RegretMinimization,
    "stakeholder_mapper": StakeholderPowerMapper,
    "opportunity_cost": OpportunityCostCalculator,
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
    "NashEquilibriumStrategist",
    "FirstPrinciplesDeconstructor",
    "SecondOrderThinking",
    "InversionSolver",
    "BayesianBeliefUpdater",
    "RegretMinimization",
    "StakeholderPowerMapper",
    "OpportunityCostCalculator",
]
