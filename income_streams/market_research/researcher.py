"""AI Market Research Reports - Income Stream #12.

Business Model: Generate comprehensive market research reports for businesses
looking to enter new markets or understand their current market landscape.
Pricing: 500-3,000 SAR per report depending on depth and market complexity.

Usage: python -m income_streams.market_research.researcher --industry "تقنية" --market "السعودية" --depth comprehensive --save
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class MarketResearcher:
    """AI-powered market research report generator for MENA markets."""

    def __init__(self):
        self.client = AIClient(module_name="market_research")

    def generate_report(self, industry: str, market: str = "السعودية", depth: str = "comprehensive") -> str:
        """Generate a full market research report.

        Args:
            industry: The industry/sector to research (e.g., "تقنية", "عقارات").
            market: Target market/country (default: Saudi Arabia).
            depth: Level of detail - "quick", "standard", or "comprehensive".

        Returns:
            Formatted market research report in Arabic.
        """
        system = (
            "أنت خبير أبحاث سوق مع 15 سنة خبرة في الأسواق العربية والخليجية. "
            "تحلل حجم السوق (TAM/SAM/SOM)، المنافسين، الاتجاهات، فرص الدخول، والمخاطر. "
            "تكتب تقارير جاهزة للمستثمرين بمستوى احترافي عالٍ مدعومة بالبيانات والإحصائيات. "
            "تقاريرك تتضمن تحليلات PESTEL وPorter's Five Forces ونماذج التقييم المعتمدة دولياً. "
            "تقدم توصيات عملية وقابلة للتنفيذ مع جداول زمنية واضحة."
        )

        depth_instructions = {
            "quick": "قدم تقريراً موجزاً يغطي النقاط الأساسية في 500-800 كلمة.",
            "standard": "قدم تقريراً متوسط التفصيل يغطي جميع المحاور في 1000-1500 كلمة.",
            "comprehensive": "قدم تقريراً شاملاً ومفصلاً يغطي كل محور بعمق في 2000-3000 كلمة مع أمثلة وبيانات.",
        }

        prompt = (
            f"أعد تقرير أبحاث سوق {depth_instructions.get(depth, depth_instructions['comprehensive'])} "
            f"عن صناعة **{industry}** في سوق **{market}**.\n\n"
            "يجب أن يتضمن التقرير المحاور التالية:\n\n"
            "1. **ملخص تنفيذي**: نظرة عامة على السوق والفرص الرئيسية\n"
            "2. **حجم السوق**: تحليل TAM (إجمالي السوق المتاح)، SAM (السوق القابل للخدمة)، "
            "SOM (السوق القابل للتحقيق) مع تقديرات بالأرقام\n"
            "3. **تحليل المنافسين**: أبرز اللاعبين، حصصهم السوقية، نقاط القوة والضعف\n"
            "4. **شرائح العملاء**: تحديد الشرائح المستهدفة وخصائصها الديموغرافية والسلوكية\n"
            "5. **قنوات التوزيع**: القنوات الأكثر فعالية للوصول للعملاء\n"
            "6. **استراتيجيات التسعير**: نماذج التسعير السائدة ومقارنة الأسعار\n"
            "7. **فرص النمو**: الفرص غير المستغلة والاتجاهات الناشئة\n"
            "8. **المخاطر والتحديات**: التحديات التنظيمية والسوقية والتشغيلية\n"
            "9. **التوصيات**: توصيات عملية مع أولويات واضحة\n"
            "10. **خطة دخول السوق**: خطوات عملية مع جدول زمني مقترح\n\n"
            "استخدم تنسيق Markdown احترافي مع جداول وعناوين واضحة."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def compare_markets(self, markets: list) -> str:
        """Compare multiple markets side by side.

        Args:
            markets: List of market names to compare (e.g., ["السعودية", "الإمارات", "مصر"]).

        Returns:
            Comparative market analysis report.
        """
        system = (
            "أنت خبير أبحاث سوق مع 15 سنة خبرة في الأسواق العربية والخليجية. "
            "تحلل حجم السوق (TAM/SAM/SOM)، المنافسين، الاتجاهات، فرص الدخول، والمخاطر. "
            "تكتب تقارير مقارنة احترافية تساعد في اتخاذ قرارات استراتيجية."
        )

        markets_str = "، ".join(markets)
        prompt = (
            f"أعد تقرير مقارنة شاملة بين الأسواق التالية: **{markets_str}**.\n\n"
            "يجب أن تشمل المقارنة:\n"
            "- حجم السوق والنمو المتوقع لكل سوق\n"
            "- سهولة الدخول والبيئة التنظيمية\n"
            "- المنافسة وتشبع السوق\n"
            "- القوة الشرائية للمستهلكين\n"
            "- البنية التحتية والتقنية\n"
            "- المخاطر الخاصة بكل سوق\n"
            "- التوصية النهائية مع ترتيب الأسواق حسب الأفضلية\n\n"
            "قدم جدول مقارنة واضح واختم بتوصية نهائية مسببة."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, industry: str, **kwargs) -> str:
        """Generate a market research report and save it to a file.

        Args:
            industry: The industry to research.
            **kwargs: Additional arguments passed to generate_report().

        Returns:
            Path to the saved report file.
        """
        content = self.generate_report(industry, **kwargs)
        filename = timestamp_filename(f"market_research_{industry}", "md")
        return save_output(content, filename, str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Market Research Reports - تقارير أبحاث السوق بالذكاء الاصطناعي"
    )
    parser.add_argument(
        "--industry", "-i", required=True, help="الصناعة/القطاع المراد دراسته (مثال: تقنية، عقارات، صحة)"
    )
    parser.add_argument(
        "--market", "-m", default="السعودية", help="السوق المستهدف (الافتراضي: السعودية)"
    )
    parser.add_argument(
        "--depth", "-d",
        choices=["quick", "standard", "comprehensive"],
        default="comprehensive",
        help="مستوى عمق التقرير (الافتراضي: comprehensive)",
    )
    parser.add_argument(
        "--save", "-s", action="store_true", help="حفظ التقرير في ملف"
    )

    args = parser.parse_args()
    researcher = MarketResearcher()

    if args.save:
        path = researcher.generate_and_save(args.industry, market=args.market, depth=args.depth)
        print(f"Saved to: {path}")
    else:
        print(researcher.generate_report(args.industry, market=args.market, depth=args.depth))


if __name__ == "__main__":
    main()
