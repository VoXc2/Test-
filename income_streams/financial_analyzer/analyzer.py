"""AI Financial Analyzer - Income Stream #13.

Business Model: Provide AI-powered financial analysis for SMEs and startups
in the Saudi and Gulf markets. Analyze revenue, expenses, profitability,
and provide actionable recommendations.
Pricing: 200-1,000 SAR per analysis depending on complexity.

Usage: python -m income_streams.financial_analyzer.analyzer --revenue 500000 --expenses 350000 --period quarterly --type "تجارة إلكترونية" --save
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class FinancialAnalyzer:
    """AI-powered financial analysis tool for businesses."""

    def __init__(self):
        self.client = AIClient(module_name="financial_analyzer")

    def analyze(self, revenue: str, expenses: str, period: str = "quarterly", business_type: str = "") -> str:
        """Analyze financial data and provide insights.

        Args:
            revenue: Total revenue amount in SAR.
            expenses: Total expenses amount in SAR.
            period: Analysis period - "monthly", "quarterly", or "annual".
            business_type: Type of business for industry benchmarking.

        Returns:
            Comprehensive financial analysis report in Arabic.
        """
        system = (
            "أنت محلل مالي معتمد (CFA) خبير في السوق السعودي والخليجي مع خبرة 12 سنة. "
            "تحلل القوائم المالية بدقة عالية وتعطي نسب مالية مهمة وتوقعات مبنية على البيانات. "
            "تقدم توصيات عملية لتحسين الأداء المالي مع مراعاة الأنظمة الضريبية السعودية (الزكاة وضريبة القيمة المضافة). "
            "تستخدم معايير المحاسبة الدولية (IFRS) والمعايير السعودية (SOCPA). "
            "تقدم تحليلات مقارنة مع متوسطات الصناعة في السوق السعودي."
        )

        business_context = f" لنشاط تجاري من نوع **{business_type}**" if business_type else ""
        prompt = (
            f"حلل البيانات المالية التالية{business_context} للفترة ({period}):\n\n"
            f"- **الإيرادات**: {revenue} ريال سعودي\n"
            f"- **المصروفات**: {expenses} ريال سعودي\n\n"
            "قدم تحليلاً مالياً شاملاً يتضمن:\n\n"
            "1. **تحليل الإيرادات والمصروفات**: توزيع وتصنيف المصروفات المتوقعة\n"
            "2. **هامش الربح**: الهامش الإجمالي والصافي ومقارنتهما بمتوسط الصناعة\n"
            "3. **نسب السيولة**: النسبة الجارية والسريعة\n"
            "4. **نقطة التعادل**: حساب نقطة التعادل والمبيعات المطلوبة لتحقيقها\n"
            "5. **التدفق النقدي**: تحليل التدفق النقدي التشغيلي والتوقعات\n"
            "6. **مقارنة بالصناعة**: مقارنة الأداء مع متوسطات الصناعة في السعودية\n"
            "7. **توصيات خفض التكاليف**: فرص محددة لتقليل المصروفات\n"
            "8. **فرص نمو الإيرادات**: استراتيجيات لزيادة الإيرادات\n"
            "9. **توقعات 12 شهر**: توقعات مالية للأشهر الـ 12 القادمة\n"
            "10. **ملخص ومؤشرات الأداء الرئيسية (KPIs)**: أهم المؤشرات التي يجب مراقبتها\n\n"
            "استخدم تنسيق Markdown مع جداول للأرقام والنسب."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_financial_report(self, data: str) -> str:
        """Generate a financial report from raw financial data text.

        Args:
            data: Raw financial data as text (e.g., pasted from spreadsheet).

        Returns:
            Structured financial analysis report.
        """
        system = (
            "أنت محلل مالي معتمد (CFA) خبير في السوق السعودي والخليجي. "
            "تحلل القوائم المالية وتستخرج النسب المالية المهمة وتقدم توصيات عملية. "
            "تقدم تحليلات مبنية على معايير IFRS والمعايير السعودية SOCPA."
        )

        prompt = (
            "حلل البيانات المالية التالية واستخرج منها تقريراً مالياً شاملاً:\n\n"
            f"{data}\n\n"
            "يجب أن يتضمن التقرير: القوائم المالية المنظمة، النسب المالية الرئيسية، "
            "تحليل الاتجاهات، نقاط القوة والضعف المالية، والتوصيات."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def forecast(self, current_data: str, months: int = 12) -> str:
        """Generate financial forecasts based on current data.

        Args:
            current_data: Current financial data description.
            months: Number of months to forecast (default: 12).

        Returns:
            Financial forecast report.
        """
        system = (
            "أنت محلل مالي معتمد (CFA) متخصص في التنبؤات المالية والنمذجة المالية. "
            "تبني نماذج توقعات مبنية على البيانات التاريخية واتجاهات السوق السعودي. "
            "تقدم سيناريوهات متعددة (متفائل، واقعي، متحفظ) مع احتمالات كل سيناريو."
        )

        prompt = (
            f"بناءً على البيانات المالية التالية، قدم توقعات مالية لمدة {months} شهراً:\n\n"
            f"{current_data}\n\n"
            "يجب أن تتضمن التوقعات:\n"
            "- ثلاثة سيناريوهات (متفائل، واقعي، متحفظ)\n"
            "- توقعات الإيرادات شهرياً\n"
            "- توقعات المصروفات\n"
            "- التدفق النقدي المتوقع\n"
            "- نقطة التعادل المتوقعة\n"
            "- المخاطر المالية المحتملة\n"
            "- التوصيات الاستراتيجية\n\n"
            "قدم جدولاً شهرياً بالأرقام المتوقعة."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, revenue: str, expenses: str, **kwargs) -> str:
        """Analyze financial data and save the report.

        Args:
            revenue: Total revenue.
            expenses: Total expenses.
            **kwargs: Additional arguments passed to analyze().

        Returns:
            Path to the saved report file.
        """
        content = self.analyze(revenue, expenses, **kwargs)
        filename = timestamp_filename("financial_analysis", "md")
        return save_output(content, filename, str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Financial Analyzer - المحلل المالي بالذكاء الاصطناعي"
    )
    parser.add_argument(
        "--revenue", "-r", required=True, help="إجمالي الإيرادات بالريال السعودي"
    )
    parser.add_argument(
        "--expenses", "-e", required=True, help="إجمالي المصروفات بالريال السعودي"
    )
    parser.add_argument(
        "--period", "-p",
        choices=["monthly", "quarterly", "annual"],
        default="quarterly",
        help="فترة التحليل (الافتراضي: quarterly)",
    )
    parser.add_argument(
        "--type", "-t", default="", dest="business_type", help="نوع النشاط التجاري"
    )
    parser.add_argument(
        "--save", "-s", action="store_true", help="حفظ التقرير في ملف"
    )

    args = parser.parse_args()
    analyzer = FinancialAnalyzer()

    if args.save:
        path = analyzer.generate_and_save(
            args.revenue, args.expenses, period=args.period, business_type=args.business_type
        )
        print(f"Saved to: {path}")
    else:
        print(analyzer.analyze(args.revenue, args.expenses, period=args.period, business_type=args.business_type))


if __name__ == "__main__":
    main()
