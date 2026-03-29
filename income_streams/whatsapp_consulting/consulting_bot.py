"""AI Business Consulting via WhatsApp - Premium Income Stream.

An AI-powered business consultant that operates through WhatsApp.
Clients pay monthly subscription for access to AI business advice.

Business Model:
- Basic: 299 SAR/month - 20 consultations
- Pro: 799 SAR/month - unlimited + reports
- Enterprise: 1,999 SAR/month - unlimited + custom + priority

Usage:
    python -m income_streams.whatsapp_consulting.consulting_bot --query "كيف أزيد مبيعاتي؟"
"""

import argparse
import json
from datetime import datetime

from income_streams.common import AIClient
from income_streams.common.utils import save_output, save_json
from income_streams.common.config_loader import get_output_dir


class ConsultingBot:
    """AI Business Consultant accessible via WhatsApp."""

    SPECIALIZATIONS = {
        "marketing": "تسويق",
        "finance": "مالية",
        "operations": "عمليات",
        "hr": "موارد بشرية",
        "strategy": "استراتيجية",
        "legal": "قانوني",
        "tech": "تقنية",
        "sales": "مبيعات",
    }

    def __init__(self):
        self.client = AIClient()

    def consult(self, query: str, business_context: str = "", specialization: str = "strategy") -> str:
        """Provide AI business consultation.

        Args:
            query: The client's business question
            business_context: Background about their business
            specialization: Area of consultation
        """
        system = f"""أنت مستشار أعمال خبير متخصص في {self.SPECIALIZATIONS.get(specialization, specialization)}.
لديك 15+ سنة خبرة في السوق السعودي والخليجي.

قواعدك:
- قدم نصائح عملية ومحددة، ليست عامة
- استخدم أمثلة من السوق السعودي/الخليجي
- اذكر أرقام وإحصائيات عند الإمكان
- قدم خطة عمل واضحة بخطوات
- نبّه على المخاطر المحتملة
- اقترح أدوات/موارد مفيدة
- كن صريحاً حتى لو الحقيقة صعبة

صيغة الإجابة:
1. تحليل سريع للموقف
2. التوصيات (مرقمة)
3. خطة العمل (الأسبوع القادم)
4. مؤشرات النجاح (KPIs)
5. تحذيرات"""

        prompt = f"""سؤال العميل: {query}

{"سياق العمل: " + business_context if business_context else ""}"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_business_report(self, business_description: str, period: str = "شهري") -> str:
        """Generate a comprehensive business analysis report."""
        system = """أنت محلل أعمال يكتب تقارير استشارية احترافية بالعربي.
التقرير يجب أن يكون شاملاً وفيه رؤى قابلة للتنفيذ."""

        prompt = f"""اكتب تقرير تحليل أعمال {period} لـ:
{business_description}

يشمل:
1. ملخص تنفيذي
2. تحليل SWOT
3. تحليل السوق والمنافسين
4. الأداء المالي (إطار عام)
5. فرص النمو
6. المخاطر والتحديات
7. التوصيات الاستراتيجية
8. خطة العمل للفترة القادمة
9. مؤشرات الأداء المقترحة"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def quick_answer(self, question: str) -> str:
        """Quick WhatsApp-friendly answer (for basic tier)."""
        system = """أجب على سؤال الأعمال بإجابة قصيرة مناسبة للواتساب.
3-5 نقاط مع إيموجي. كن مفيداً ومحدداً."""

        return self.client.generate(question, system_prompt=system, max_tokens=500)

    def analyze_competitors(self, business: str, competitors: str) -> str:
        """Analyze competitors for a business."""
        system = "أنت محلل تنافسي خبير في السوق السعودي."

        prompt = f"""حلل المنافسة لـ: {business}
المنافسين: {competitors}

أعطني:
1. مقارنة تفصيلية
2. نقاط القوة/الضعف لكل منافس
3. الفجوات في السوق
4. استراتيجيات التميز
5. فرص لم يستغلها المنافسون"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)


def main():
    parser = argparse.ArgumentParser(description="AI Business Consultant - مستشار أعمال ذكي")
    parser.add_argument("--query", "-q", help="Business question")
    parser.add_argument("--context", "-c", default="", help="Business context")
    parser.add_argument("--spec", "-s", default="strategy",
                        choices=list(ConsultingBot.SPECIALIZATIONS.keys()))
    parser.add_argument("--report", "-r", help="Generate business report")
    parser.add_argument("--competitors", nargs=2, metavar=("BUSINESS", "COMPETITORS"),
                        help="Competitor analysis")

    args = parser.parse_args()
    bot = ConsultingBot()

    if args.report:
        print(bot.generate_business_report(args.report))
    elif args.competitors:
        print(bot.analyze_competitors(args.competitors[0], args.competitors[1]))
    elif args.query:
        print(bot.consult(args.query, args.context, args.spec))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
