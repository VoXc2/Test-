"""AI Project Estimator.

Smart project estimation that considers complexity, features, and market rates.
"""

from income_streams.common import AIClient


class ProjectEstimator:
    """Estimate project costs and timelines using AI."""

    def __init__(self):
        self.client = AIClient()

    def estimate(self, description: str, budget_range: str = "متوسط") -> str:
        """Generate detailed project estimate."""
        system = """أنت خبير تقدير مشاريع برمجية بـ 10+ سنوات خبرة في السوق السعودي والخليجي.
تعطي تقديرات واقعية ودقيقة.

أسعار السوق السعودي 2024-2026:
- مطور جونيور: 150-250 ر.س/ساعة
- مطور سينيور: 300-500 ر.س/ساعة
- مصمم UI/UX: 200-400 ر.س/ساعة
- مدير مشروع: 200-350 ر.س/ساعة"""

        prompt = f"""قدّر المشروع التالي:
الوصف: {description}
ميزانية العميل: {budget_range}

أعطني:
1. تفصيل الساعات لكل مرحلة
2. عدد المطورين المطلوبين
3. التكلفة التفصيلية
4. الجدول الزمني
5. المخاطر المحتملة
6. توصيات لتقليل التكلفة"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)
