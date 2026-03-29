"""AI Real Estate Analysis Tool - Saudi Market Focus.

Analyze real estate investments, property valuations, and market trends
specifically for the Saudi Arabian market (Vision 2030, NEOM, mega projects).

Business Model:
- Sell reports to investors: 500-2000 SAR per report
- Monthly subscription for agents: 999 SAR/month
- Partnership with real estate agencies

Usage:
    python -m income_streams.real_estate_analyzer.analyzer --type investment --location "الرياض - حي النرجس"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.utils import save_output, timestamp_filename
from income_streams.common.config_loader import get_output_dir


class RealEstateAnalyzer:
    """AI-powered real estate analysis for the Saudi market."""

    def __init__(self):
        self.client = AIClient()

    def analyze_investment(self, location: str, property_type: str = "سكني",
                           budget: str = "", purpose: str = "استثمار") -> str:
        """Generate comprehensive investment analysis."""
        system = """أنت محلل عقاري خبير في السوق السعودي. لديك معرفة عميقة بـ:
- أسعار العقارات في جميع مدن ومناطق المملكة
- رؤية 2030 وتأثيرها على السوق العقاري
- المشاريع الضخمة (نيوم، ذا لاين، القدية، مشروع البحر الأحمر)
- أنظمة وزارة الإسكان والصندوق العقاري
- معدلات العائد على الاستثمار العقاري
- اتجاهات السوق والتوقعات

أعطِ تحليلات واقعية مبنية على بيانات السوق."""

        prompt = f"""حلل الفرصة العقارية التالية:

الموقع: {location}
نوع العقار: {property_type}
الميزانية: {budget or 'غير محددة'}
الهدف: {purpose}

التحليل يشمل:
1. **نظرة عامة على المنطقة**: البنية التحتية، الخدمات، المشاريع القريبة
2. **تحليل الأسعار**: متوسط سعر المتر، مقارنة بالأحياء المجاورة، اتجاه الأسعار
3. **العائد على الاستثمار**: العائد الإيجاري المتوقع، نمو رأس المال
4. **تأثير رؤية 2030**: المشاريع الحكومية القريبة وتأثيرها
5. **المخاطر**: عوامل قد تؤثر سلبًا
6. **التوصيات**: شراء/انتظار/بديل أفضل
7. **السيناريوهات**: متفائل/متوسط/متشائم (3-5 سنوات)
8. **نصائح التفاوض**: كيف تحصل على أفضل سعر
9. **الإجراءات القانونية**: ما تحتاج معرفته
10. **الحكم النهائي**: تقييم من 10 مع التبرير"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def compare_properties(self, properties: list) -> str:
        """Compare multiple properties side by side."""
        system = "أنت محلل عقاري يقارن بين العقارات بشكل موضوعي ومفصل."

        props_text = "\n".join(f"عقار {i+1}: {p}" for i, p in enumerate(properties))
        prompt = f"""قارن بين هذه العقارات:
{props_text}

أعطني:
1. جدول مقارنة شامل
2. إيجابيات وسلبيات كل عقار
3. أيهم أفضل للسكن
4. أيهم أفضل للاستثمار
5. التوصية النهائية"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def market_report(self, city: str, quarter: str = "الربع الحالي") -> str:
        """Generate a market report for a city."""
        system = """أنت محلل سوق عقاري يكتب تقارير احترافية عن السوق السعودي.
اكتب التقرير بأسلوب احترافي مناسب للمستثمرين."""

        prompt = f"""اكتب تقرير سوق عقاري لـ {city} - {quarter}

يشمل:
1. ملخص تنفيذي
2. حالة السوق الحالية
3. متوسط الأسعار حسب الحي والنوع
4. حجم الصفقات
5. المشاريع الجديدة
6. العوامل المؤثرة
7. التوقعات للربع القادم
8. فرص استثمارية
9. مناطق يجب تجنبها
10. توصيات عملية"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, analysis_type: str, **kwargs) -> str:
        """Generate analysis and save to file."""
        if analysis_type == "investment":
            content = self.analyze_investment(**kwargs)
        elif analysis_type == "market":
            content = self.market_report(**kwargs)
        else:
            content = self.analyze_investment(**kwargs)

        output_dir = get_output_dir("reports")
        filename = timestamp_filename(f"real_estate_{analysis_type}", "md")
        return save_output(content, filename, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="Real Estate Analyzer - محلل عقاري ذكي")
    parser.add_argument("--type", "-t", default="investment",
                        choices=["investment", "market", "compare"])
    parser.add_argument("--location", "-l", help="Property location")
    parser.add_argument("--property-type", "-p", default="سكني", help="Property type")
    parser.add_argument("--budget", "-b", default="", help="Budget")
    parser.add_argument("--city", "-c", help="City for market report")
    parser.add_argument("--save", "-s", action="store_true")

    args = parser.parse_args()
    analyzer = RealEstateAnalyzer()

    if args.type == "investment" and args.location:
        result = analyzer.analyze_investment(args.location, args.property_type, args.budget)
        print(result)
    elif args.type == "market" and args.city:
        result = analyzer.market_report(args.city)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
