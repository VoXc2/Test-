"""Test that all 60 income stream modules + 14 prompt frameworks import without errors."""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_import_common():
    from income_streams.common.config_loader import get_config, load_env
    from income_streams.common.utils import slugify, word_count, truncate, timestamp_filename
    assert slugify("Hello World") == "hello-world"
    assert word_count("one two three") == 3
    assert truncate("hello", 10) == "hello"
    assert truncate("hello world", 8) == "hello..."


# === Original 11 modules ===

def test_import_content_generation():
    from income_streams.content_generation import BlogGenerator, SocialMediaGenerator, NewsletterGenerator
    assert BlogGenerator() is not None

def test_import_translation():
    from income_streams.translation_service import Translator, BatchTranslator
    assert Translator() is not None

def test_import_freelance():
    from income_streams.freelance_proposals import ProposalGenerator
    assert ProposalGenerator() is not None

def test_import_cv_builder():
    from income_streams.cv_builder import CVGenerator
    assert CVGenerator() is not None

def test_import_micro_saas():
    from income_streams.micro_saas.tools.text_summarizer import TextSummarizer
    from income_streams.micro_saas.tools.email_writer import EmailWriter
    from income_streams.micro_saas.tools.grammar_checker import GrammarChecker
    assert TextSummarizer() is not None

def test_import_prompt_marketplace():
    from income_streams.prompt_marketplace import PromptManager
    pm = PromptManager()
    assert pm.get_stats()["total_prompts"] >= 10

def test_import_support():
    from income_streams.whatsapp_support import CustomerSupportBot
    assert CustomerSupportBot() is not None

def test_import_app_agency():
    from income_streams.app_agency import AgencyManager, WhatsAppClientBot, ProjectEstimator
    assert AgencyManager() is not None

def test_import_consulting():
    from income_streams.whatsapp_consulting import ConsultingBot
    assert ConsultingBot() is not None

def test_import_real_estate():
    from income_streams.real_estate_analyzer import RealEstateAnalyzer
    assert RealEstateAnalyzer() is not None

def test_import_legal():
    from income_streams.legal_documents import LegalDocumentGenerator
    assert len(LegalDocumentGenerator().DOCUMENT_TYPES) >= 10

def test_import_ecommerce():
    from income_streams.ecommerce_engine import ProductDescriptionEngine
    assert ProductDescriptionEngine() is not None


# === Batch 1: Data & Analytics (12-16) ===

def test_import_market_research():
    from income_streams.market_research import MarketResearcher
    assert MarketResearcher() is not None

def test_import_financial_analyzer():
    from income_streams.financial_analyzer import FinancialAnalyzer
    assert FinancialAnalyzer() is not None

def test_import_survey_analyzer():
    from income_streams.survey_analyzer import SurveyAnalyzer
    assert SurveyAnalyzer() is not None

def test_import_social_analytics():
    from income_streams.social_analytics import SocialAnalytics
    assert SocialAnalytics() is not None

def test_import_competitor_tracker():
    from income_streams.competitor_tracker import CompetitorTracker
    assert CompetitorTracker() is not None


# === Batch 1: Design & Creative (17-21) ===

def test_import_presentation_builder():
    from income_streams.presentation_builder import PresentationBuilder
    assert PresentationBuilder() is not None

def test_import_video_scripts():
    from income_streams.video_scripts import VideoScriptGenerator
    assert VideoScriptGenerator() is not None

def test_import_podcast_producer():
    from income_streams.podcast_producer import PodcastProducer
    assert PodcastProducer() is not None

def test_import_brand_identity():
    from income_streams.brand_identity import BrandIdentityGenerator
    assert BrandIdentityGenerator() is not None

def test_import_infographic():
    from income_streams.infographic_engine import InfographicGenerator
    assert InfographicGenerator() is not None


# === Batch 2: Education (22-26) ===

def test_import_course_creator():
    from income_streams.course_creator import CourseCreator
    assert CourseCreator() is not None

def test_import_quiz_generator():
    from income_streams.quiz_generator import QuizGenerator
    assert QuizGenerator() is not None

def test_import_tutoring_bot():
    from income_streams.tutoring_bot import TutoringBot
    assert TutoringBot() is not None

def test_import_study_notes():
    from income_streams.study_notes import StudyNotesGenerator
    assert StudyNotesGenerator() is not None

def test_import_training_programs():
    from income_streams.training_programs import TrainingProgramBuilder
    assert TrainingProgramBuilder() is not None


# === Batch 2: Health & Wellness (27-29) ===

def test_import_meal_planner():
    from income_streams.meal_planner import MealPlanner
    assert MealPlanner() is not None

def test_import_fitness_coach():
    from income_streams.fitness_coach import FitnessCoach
    assert FitnessCoach() is not None

def test_import_wellness_bot():
    from income_streams.wellness_bot import WellnessBot
    assert WellnessBot() is not None


# === Batch 2: HR (30-33) ===

def test_import_job_descriptions():
    from income_streams.job_descriptions import JobDescriptionGenerator
    assert JobDescriptionGenerator() is not None

def test_import_interview_kit():
    from income_streams.interview_kit import InterviewKitGenerator
    assert InterviewKitGenerator() is not None

def test_import_onboarding():
    from income_streams.onboarding_generator import OnboardingGenerator
    assert OnboardingGenerator() is not None

def test_import_performance_reviews():
    from income_streams.performance_reviews import PerformanceReviewWriter
    assert PerformanceReviewWriter() is not None


# === Batch 3: Finance (34-36) ===

def test_import_invoice():
    from income_streams.invoice_generator import InvoiceGenerator
    assert InvoiceGenerator() is not None

def test_import_budget_planner():
    from income_streams.budget_planner import BudgetPlanner
    assert BudgetPlanner() is not None

def test_import_tax_guide():
    from income_streams.tax_guide import TaxGuide
    assert TaxGuide() is not None


# === Batch 3: Food (37-39) ===

def test_import_menu_designer():
    from income_streams.menu_designer import MenuDesigner
    assert MenuDesigner() is not None

def test_import_review_responder():
    from income_streams.review_responder import ReviewResponder
    assert ReviewResponder() is not None

def test_import_recipe_creator():
    from income_streams.recipe_creator import RecipeCreator
    assert RecipeCreator() is not None


# === Batch 3: Travel & Events (40-42) ===

def test_import_travel_planner():
    from income_streams.travel_planner import TravelPlanner
    assert TravelPlanner() is not None

def test_import_event_planner():
    from income_streams.event_planner import EventPlanner
    assert EventPlanner() is not None

def test_import_invitation_writer():
    from income_streams.invitation_writer import InvitationWriter
    assert InvitationWriter() is not None


# === Batch 4: Social Media (43-46) ===

def test_import_hashtag_strategist():
    from income_streams.hashtag_strategist import HashtagStrategist
    assert HashtagStrategist() is not None

def test_import_youtube_optimizer():
    from income_streams.youtube_optimizer import YouTubeOptimizer
    assert YouTubeOptimizer() is not None

def test_import_tiktok_scripts():
    from income_streams.tiktok_scripts import TikTokScriptWriter
    assert TikTokScriptWriter() is not None

def test_import_content_calendar():
    from income_streams.content_calendar import ContentCalendarGenerator
    assert ContentCalendarGenerator() is not None


# === Batch 4: Specialized (47-50) ===

def test_import_car_listings():
    from income_streams.car_listings import CarListingWriter
    assert CarListingWriter() is not None

def test_import_academic_assistant():
    from income_streams.academic_assistant import AcademicAssistant
    assert AcademicAssistant() is not None

def test_import_grant_proposals():
    from income_streams.grant_proposals import GrantProposalWriter
    assert GrantProposalWriter() is not None

def test_import_feedback_analyzer():
    from income_streams.feedback_analyzer import FeedbackAnalyzer
    assert FeedbackAnalyzer() is not None


# === Batch 5: Marketing & Sales (51-60) ===

def test_import_email_sequences():
    from income_streams.email_sequences import EmailSequenceGenerator
    assert EmailSequenceGenerator() is not None

def test_import_sales_funnel():
    from income_streams.sales_funnel import SalesFunnelBuilder
    assert SalesFunnelBuilder() is not None

def test_import_landing_page_copy():
    from income_streams.landing_page_copy import LandingPageCopyGenerator
    assert LandingPageCopyGenerator() is not None

def test_import_ad_copy_generator():
    from income_streams.ad_copy_generator import AdCopyGenerator
    assert AdCopyGenerator() is not None

def test_import_lead_magnet_creator():
    from income_streams.lead_magnet_creator import LeadMagnetCreator
    assert LeadMagnetCreator() is not None

def test_import_pricing_optimizer():
    from income_streams.pricing_optimizer import PricingStrategyOptimizer
    assert PricingStrategyOptimizer() is not None

def test_import_customer_journey():
    from income_streams.customer_journey import CustomerJourneyMapper
    assert CustomerJourneyMapper() is not None

def test_import_affiliate_program():
    from income_streams.affiliate_program import AffiliateProgramBuilder
    assert AffiliateProgramBuilder() is not None

def test_import_launch_sequence():
    from income_streams.launch_sequence import LaunchSequencePlanner
    assert LaunchSequencePlanner() is not None

def test_import_seo_optimizer():
    from income_streams.seo_optimizer import SEOContentOptimizer
    assert SEOContentOptimizer() is not None


# === Prompt Frameworks ===

def test_import_frameworks():
    from prompt_frameworks import FRAMEWORKS
    assert len(FRAMEWORKS) == 14

def test_framework_info():
    from prompt_frameworks import FRAMEWORKS
    for name, cls in FRAMEWORKS.items():
        fw = cls()
        info = fw.info()
        assert info["name"] != ""
        assert info["name_ar"] != ""
        assert len(info["required_inputs"]) > 0

def test_prompt_catalog():
    from income_streams.prompt_marketplace import PromptManager
    pm = PromptManager()
    assert len(pm.list_all()) >= 10
    assert len(pm.search("SEO")) > 0
    assert len(pm.get_categories()) >= 4

def test_utils():
    from income_streams.common.utils import slugify, timestamp_filename
    assert slugify("Hello World!") == "hello-world"
    fn = timestamp_filename("test", "md")
    assert fn.endswith(".md")
