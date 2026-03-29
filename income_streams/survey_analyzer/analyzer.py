"""AI Survey Analyzer - Income Stream #14.

Business Model: Analyze survey data and extract actionable insights for businesses.
Process quantitative and qualitative survey responses to identify patterns,
correlations, and provide recommendations.
Pricing: 300-800 SAR per analysis.

Usage: python -m income_streams.survey_analyzer.analyzer --data "بيانات الاستبيان..." --context "سياق العمل" --save
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class SurveyAnalyzer:
    """AI-powered survey data analysis and insights generator."""

    def __init__(self):
        self.client = AIClient(module_name="survey_analyzer")

    def analyze(self, survey_data: str, context: str = "") -> str:
        """Analyze survey data and generate comprehensive insights.

        Args:
            survey_data: Survey description, questions, and results as text.
            context: Optional business context for more relevant analysis.

        Returns:
            Detailed survey analysis report in Arabic.
        """
        system = (
            "أنت خبير تحليل استبيانات وبحوث كمية ونوعية مع خبرة 10 سنوات في السوق العربي. "
            "تستخرج أنماطاً من البيانات، تحدد ارتباطات وعلاقات سببية، وتقدم رؤى عملية قابلة للتنفيذ. "
            "تستخدم أساليب التحليل الإحصائي مثل التحليل العنقودي وتحليل الانحدار والتحليل العاملي. "
            "تقدم نتائجك بأسلوب واضح يفهمه أصحاب القرار غير المتخصصين في الإحصاء. "
            "تربط النتائج بتوصيات عملية محددة تساعد في تحسين المنتجات والخدمات."
        )

        context_section = f"\n**سياق العمل**: {context}\n" if context else ""
        prompt = (
            f"حلل بيانات الاستبيان التالية وقدم تقريراً شاملاً بالرؤى والتوصيات:\n"
            f"{context_section}\n"
            f"**بيانات الاستبيان**:\n{survey_data}\n\n"
            "يجب أن يتضمن التقرير:\n\n"
            "1. **ملخص تنفيذي**: أهم النتائج والرؤى في فقرة واحدة\n"
            "2. **تحليل كل سؤال**: تفصيل النتائج لكل سؤال مع النسب والتفسير\n"
            "3. **الأنماط الرئيسية**: الأنماط والاتجاهات المكتشفة في البيانات\n"
            "4. **مقارنة الشرائح**: الفروقات بين شرائح المستجيبين المختلفة\n"
            "5. **الرؤى المفاجئة**: نتائج غير متوقعة أو مثيرة للاهتمام\n"
            "6. **التوصيات العملية**: إجراءات محددة مبنية على النتائج مع أولويات\n"
            "7. **نقاط القوة والضعف المكتشفة**: ما يعمل بشكل جيد وما يحتاج تحسين\n"
            "8. **الخطوات التالية**: اقتراحات لاستبيانات أو أبحاث إضافية مطلوبة\n\n"
            "استخدم تنسيق Markdown مع رسوم بيانية نصية إن أمكن."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_insights(self, responses: str) -> str:
        """Generate quick insights from survey responses.

        Args:
            responses: Raw survey responses as text.

        Returns:
            Key insights and actionable recommendations.
        """
        system = (
            "أنت خبير تحليل استبيانات وبحوث كمية ونوعية. "
            "تستخرج الرؤى الرئيسية بسرعة من بيانات الاستبيانات وتحولها لتوصيات عملية. "
            "تركز على الأنماط الأهم والأكثر تأثيراً على القرارات التجارية."
        )

        prompt = (
            "استخرج أهم الرؤى والملاحظات من ردود الاستبيان التالية:\n\n"
            f"{responses}\n\n"
            "قدم:\n"
            "- أهم 5 رؤى رئيسية\n"
            "- الأنماط المتكررة\n"
            "- النقاط التي تحتاج اهتماماً فورياً\n"
            "- 3-5 توصيات عملية مرتبة حسب الأولوية\n"
            "- ملخص تنفيذي من سطرين"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, survey_data: str, **kwargs) -> str:
        """Analyze survey data and save the report.

        Args:
            survey_data: Survey data to analyze.
            **kwargs: Additional arguments passed to analyze().

        Returns:
            Path to the saved report file.
        """
        content = self.analyze(survey_data, **kwargs)
        filename = timestamp_filename("survey_analysis", "md")
        return save_output(content, filename, str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Survey Analyzer - محلل الاستبيانات بالذكاء الاصطناعي"
    )
    parser.add_argument(
        "--data", "-d", required=True, help="بيانات الاستبيان (وصف الأسئلة والنتائج كنص)"
    )
    parser.add_argument(
        "--context", "-c", default="", help="سياق العمل (اختياري، مثال: متجر إلكتروني)"
    )
    parser.add_argument(
        "--save", "-s", action="store_true", help="حفظ التقرير في ملف"
    )

    args = parser.parse_args()
    analyzer = SurveyAnalyzer()

    if args.save:
        path = analyzer.generate_and_save(args.data, context=args.context)
        print(f"Saved to: {path}")
    else:
        print(analyzer.analyze(args.data, context=args.context))


if __name__ == "__main__":
    main()
