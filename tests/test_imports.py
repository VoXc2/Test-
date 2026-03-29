"""Test that all modules can be imported without errors."""

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


def test_import_content_generation():
    from income_streams.content_generation import BlogGenerator, SocialMediaGenerator, NewsletterGenerator
    gen = BlogGenerator()
    assert gen is not None


def test_import_translation():
    from income_streams.translation_service import Translator, BatchTranslator
    t = Translator()
    assert t is not None


def test_import_freelance():
    from income_streams.freelance_proposals import ProposalGenerator
    gen = ProposalGenerator()
    assert gen is not None


def test_import_prompt_marketplace():
    from income_streams.prompt_marketplace import PromptManager
    pm = PromptManager()
    stats = pm.get_stats()
    assert stats["total_prompts"] > 0
    assert "writing" in stats["categories"]


def test_import_app_agency():
    from income_streams.app_agency import AgencyManager, WhatsAppClientBot, ProjectEstimator
    assert AgencyManager() is not None


def test_import_consulting():
    from income_streams.whatsapp_consulting import ConsultingBot
    assert ConsultingBot() is not None


def test_import_real_estate():
    from income_streams.real_estate_analyzer import RealEstateAnalyzer
    assert RealEstateAnalyzer() is not None


def test_import_cv_builder():
    from income_streams.cv_builder import CVGenerator
    assert CVGenerator() is not None


def test_import_legal():
    from income_streams.legal_documents import LegalDocumentGenerator
    gen = LegalDocumentGenerator()
    assert len(gen.DOCUMENT_TYPES) >= 10


def test_import_ecommerce():
    from income_streams.ecommerce_engine import ProductDescriptionEngine
    assert ProductDescriptionEngine() is not None


def test_import_support():
    from income_streams.whatsapp_support import CustomerSupportBot
    assert CustomerSupportBot() is not None


def test_import_frameworks():
    from prompt_frameworks import FRAMEWORKS
    assert len(FRAMEWORKS) == 6
    assert "career_survival" in FRAMEWORKS
    assert "constitutional_reasoning" in FRAMEWORKS
    assert "deep_thinking" in FRAMEWORKS


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
    all_prompts = pm.list_all()
    assert len(all_prompts) >= 10

    # Test search
    results = pm.search("SEO")
    assert len(results) > 0

    # Test categories
    cats = pm.get_categories()
    assert len(cats) >= 4


def test_utils():
    from income_streams.common.utils import slugify, timestamp_filename
    assert slugify("Hello World!") == "hello-world"
    assert slugify("مرحبا بالعالم") == "مرحبا-بالعالم"
    fn = timestamp_filename("test", "md")
    assert fn.endswith(".md")
    assert "test" in fn
