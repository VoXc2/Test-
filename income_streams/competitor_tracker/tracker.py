"""AI Competitor Tracker - Income Stream #16.

Business Model: Track and analyze competitors for businesses in the Saudi
and Gulf markets. Provide SWOT analysis, pricing comparisons, and
competitive positioning strategies.
Pricing: 999 SAR/month subscription.

Usage: python -m income_streams.competitor_tracker.tracker --business "متجر إلكتروني" --competitors "نون،أمازون،جرير" --industry "تجارة إلكترونية" --save
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class CompetitorTracker:
    """AI-powered competitive intelligence and tracking tool."""

    def __init__(self):
        self.client = AIClient(module_name="competitor_tracker")

    def track(self, business: str, competitors: str, industry: str = "") -> str:
        """Generate a comprehensive competitive analysis report.

        Args:
            business: Your business name/description.
            competitors: Comma-separated list of competitor names.
            industry: Optional industry context.

        Returns:
            Detailed competitive analysis report in Arabic.
        """
        system = (
            "أنت محلل تنافسي استراتيجي متخصص في السوق السعودي والخليجي مع 12 سنة خبرة. "
            "ترصد المنافسين وتحلل استراتيجياتهم بدقة وتحدد الفرص والتهديدات. "
            "تستخدم أطر عمل معتمدة مثل Porter's Five Forces وBlue Ocean Strategy والتحليل الرباعي SWOT. "
            "تقدم رؤى استراتيجية مبنية على فهم عميق للسوق المحلي والمنافسة الإقليمية. "
            "تساعد الشركات في بناء ميزات تنافسية مستدامة وصعبة التقليد."
        )

        industry_section = f" في قطاع **{industry}**" if industry else ""
        competitors_list = [c.strip() for c in competitors.split(",")]
        competitors_formatted = "، ".join(competitors_list)

        prompt = (
            f"أعد تقرير تحليل تنافسي شامل لعمل **{business}**{industry_section}.\n"
            f"المنافسون المراد تحليلهم: **{competitors_formatted}**\n\n"
            "يجب أن يتضمن التقرير:\n\n"
            "1. **خريطة المنافسين**: تصنيف المنافسين (مباشرين، غير مباشرين، بدلاء) "
            "مع تحديد موقع كل منافس في السوق\n"
            "2. **تحليل SWOT لكل منافس**: نقاط القوة والضعف والفرص والتهديدات\n"
            "3. **مقارنة الأسعار**: جدول مقارنة أسعار المنتجات/الخدمات الرئيسية\n"
            "4. **مقارنة المميزات**: جدول مقارنة المميزات والخدمات لكل منافس\n"
            "5. **تحليل قنوات التسويق**: القنوات التسويقية المستخدمة وفعاليتها\n"
            "6. **نقاط الضعف القابلة للاستغلال**: فجوات في السوق يمكن استغلالها\n"
            "7. **استراتيجيات التميز**: كيف تتميز عن كل منافس بشكل محدد\n"
            "8. **خطة عمل تنافسية**: خطة عمل مفصلة بخطوات وأولويات وجدول زمني\n\n"
            "استخدم تنسيق Markdown مع جداول مقارنة واضحة ومخططات نصية."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def swot_analysis(self, business: str, competitor: str) -> str:
        """Generate a detailed SWOT analysis comparing your business with a competitor.

        Args:
            business: Your business name/description.
            competitor: Competitor name to analyze.

        Returns:
            Detailed SWOT comparison report.
        """
        system = (
            "أنت محلل تنافسي استراتيجي متخصص في السوق السعودي والخليجي. "
            "تقدم تحليلات SWOT معمقة ومقارنة مع توصيات استراتيجية عملية."
        )

        prompt = (
            f"أعد تحليل SWOT مقارن بين **{business}** والمنافس **{competitor}**:\n\n"
            "لكل طرف قدم:\n"
            "- **نقاط القوة (Strengths)**: 5-7 نقاط مع شرح\n"
            "- **نقاط الضعف (Weaknesses)**: 5-7 نقاط مع شرح\n"
            "- **الفرص (Opportunities)**: 5-7 فرص مع كيفية استغلالها\n"
            "- **التهديدات (Threats)**: 5-7 تهديدات مع استراتيجيات التخفيف\n\n"
            "ثم قدم:\n"
            "- جدول مقارنة جنباً إلى جنب\n"
            "- الفجوات التنافسية\n"
            "- استراتيجيات مقترحة للتفوق\n"
            "- خطة عمل بأولويات واضحة"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def pricing_analysis(self, business: str, competitors: str) -> str:
        """Analyze and compare pricing strategies.

        Args:
            business: Your business name/description.
            competitors: Comma-separated list of competitor names.

        Returns:
            Pricing analysis and recommendations.
        """
        system = (
            "أنت محلل تنافسي متخصص في استراتيجيات التسعير في السوق السعودي والخليجي. "
            "تحلل نماذج التسعير وتقدم توصيات مبنية على القيمة والمنافسة وسلوك المستهلك."
        )

        competitors_list = [c.strip() for c in competitors.split(",")]
        competitors_formatted = "، ".join(competitors_list)

        prompt = (
            f"حلل استراتيجيات التسعير لعمل **{business}** مقارنة بالمنافسين: **{competitors_formatted}**\n\n"
            "قدم:\n"
            "- جدول مقارنة أسعار تفصيلي\n"
            "- تحليل نماذج التسعير المستخدمة (اشتراك، لكل استخدام، مجاني+مدفوع)\n"
            "- تحليل القيمة مقابل السعر\n"
            "- الفجوات السعرية في السوق\n"
            "- استراتيجية التسعير المقترحة\n"
            "- سيناريوهات تسعير مختلفة مع التأثير المتوقع على الإيرادات\n"
            "- توصيات العروض والباقات"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, business: str, competitors: str, **kwargs) -> str:
        """Track competitors and save the report.

        Args:
            business: Your business name.
            competitors: Comma-separated competitor names.
            **kwargs: Additional arguments passed to track().

        Returns:
            Path to the saved report file.
        """
        content = self.track(business, competitors, **kwargs)
        filename = timestamp_filename(f"competitor_analysis_{business}", "md")
        return save_output(content, filename, str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Competitor Tracker - متتبع المنافسين بالذكاء الاصطناعي"
    )
    parser.add_argument(
        "--business", "-b", required=True, help="اسم/وصف نشاطك التجاري"
    )
    parser.add_argument(
        "--competitors", "-c", required=True, help="أسماء المنافسين مفصولة بفواصل"
    )
    parser.add_argument(
        "--industry", "-i", default="", help="القطاع/الصناعة (اختياري)"
    )
    parser.add_argument(
        "--save", "-s", action="store_true", help="حفظ التقرير في ملف"
    )

    args = parser.parse_args()
    tracker = CompetitorTracker()

    if args.save:
        path = tracker.generate_and_save(args.business, args.competitors, industry=args.industry)
        print(f"Saved to: {path}")
    else:
        print(tracker.track(args.business, args.competitors, industry=args.industry))


if __name__ == "__main__":
    main()
