"""AI Feedback Analyzer - Income Stream #50.
Business Model: تحليل تعليقات وآراء العملاء بالذكاء الاصطناعي
Usage: python -m income_streams.feedback_analyzer.analyzer --feedback "الخدمة ممتازة لكن التوصيل بطيء" --business "مطعم" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class FeedbackAnalyzer:
    def __init__(self):
        self.client = AIClient(module_name="feedback_analyzer")

    def analyze(self, feedback_text: str, business: str = "", language: str = "ar") -> str:
        system = (
            "محلل تجربة عملاء وخبير في Voice of Customer (VoC). "
            "يحلل التعليقات ويستخرج أنماط ورؤى عملية. "
            "يصنف المشاعر ويحدد الأولويات. "
            "يفهم اللهجات العربية والخليجية ويستطيع تحليل المشاعر فيها. "
            "يقدم توصيات عملية قابلة للتنفيذ مرتبة حسب الأثر والسهولة."
        )
        lang_instruction = "قدم التحليل باللغة العربية." if language == "ar" else "Present analysis in English."
        business_section = f"\nنوع النشاط: {business}" if business else ""
        prompt = (
            f"حلل التعليق/التعليقات التالية:\n\n"
            f"---\n{feedback_text}\n---\n"
            f"{business_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. تحليل المشاعر (Sentiment Analysis)\n"
            f"- التصنيف العام: إيجابي / سلبي / محايد / مختلط\n"
            f"- درجة المشاعر (1-10)\n"
            f"- المشاعر الفرعية (رضا، إحباط، غضب، فرح، إلخ)\n"
            f"- العبارات الدالة على كل مشاعر\n\n"
            f"## 2. المواضيع الرئيسية\n"
            f"- استخراج المواضيع المذكورة\n"
            f"- تصنيفها (منتج، خدمة، سعر، توصيل، دعم، إلخ)\n"
            f"- تكرار كل موضوع\n\n"
            f"## 3. المشاكل المتكررة\n"
            f"- قائمة المشاكل المذكورة\n"
            f"- خطورة كل مشكلة (عالية/متوسطة/منخفضة)\n"
            f"- تأثيرها على رضا العميل\n\n"
            f"## 4. نقاط القوة\n"
            f"- ما أعجب العملاء\n"
            f"- نقاط التميز التي يجب الحفاظ عليها\n\n"
            f"## 5. توصيات التحسين (مرتبة بالأولوية)\n"
            f"لكل توصية:\n"
            f"- التوصية\n"
            f"- الأولوية (عاجل/مهم/تحسين)\n"
            f"- سهولة التنفيذ (سهل/متوسط/صعب)\n"
            f"- الأثر المتوقع\n"
            f"- خطوات التنفيذ\n\n"
            f"## 6. مؤشرات رضا العملاء\n"
            f"- NPS المقدر (Net Promoter Score)\n"
            f"- CSAT المقدر (Customer Satisfaction)\n"
            f"- CES المقدر (Customer Effort Score)\n\n"
            f"## 7. خطة عمل\n"
            f"- إجراءات فورية (هذا الأسبوع)\n"
            f"- إجراءات قصيرة المدى (هذا الشهر)\n"
            f"- إجراءات طويلة المدى (3-6 أشهر)\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def analyze_batch(self, feedbacks: str) -> str:
        system = (
            "محلل تجربة عملاء خبير في تحليل كميات كبيرة من التعليقات واستخراج الأنماط. "
            "يقدم تحليل إحصائي شامل مع رؤى عملية."
        )
        feedback_list = [f.strip() for f in feedbacks.split("---") if f.strip()]
        formatted = "\n---\n".join(f"تعليق {i+1}: {fb}" for i, fb in enumerate(feedback_list))
        prompt = (
            f"حلل مجموعة التعليقات التالية ({len(feedback_list)} تعليق):\n\n"
            f"{formatted}\n\n"
            f"قدم تحليل شامل يتضمن:\n"
            f"- نسبة المشاعر الإيجابية vs السلبية vs المحايدة\n"
            f"- أكثر المواضيع تكراراً\n"
            f"- أبرز المشاكل المشتركة\n"
            f"- أبرز نقاط القوة المشتركة\n"
            f"- Word Cloud (أكثر الكلمات تكراراً)\n"
            f"- توصيات مرتبة بالأولوية\n"
            f"- ملخص تنفيذي للإدارة\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_action_plan(self, analysis: str) -> str:
        system = (
            "مستشار تجربة عملاء يحوّل التحليلات إلى خطط عمل عملية وقابلة للتنفيذ. "
            "يرتب الإجراءات حسب الأثر وسهولة التنفيذ."
        )
        prompt = (
            f"بناءً على التحليل التالي، أعد خطة عمل تفصيلية:\n\n"
            f"{analysis[:3000]}\n\n"
            f"قدم:\n"
            f"- مصفوفة الأثر vs الجهد (4 أرباع)\n"
            f"- Quick Wins (أثر عالي + جهد قليل)\n"
            f"- مشاريع استراتيجية (أثر عالي + جهد عالي)\n"
            f"- تحسينات تدريجية\n"
            f"- جدول زمني للتنفيذ\n"
            f"- المسؤوليات والموارد المطلوبة\n"
            f"- مؤشرات قياس النجاح\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_and_save(self, feedback_text: str, **kw) -> str:
        content = self.analyze(feedback_text, **kw)
        return save_output(content, timestamp_filename("feedback_analysis", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Feedback Analyzer - تحليل تعليقات العملاء بالذكاء الاصطناعي")
    parser.add_argument("--feedback", required=True, help="نص التعليق أو التعليقات (فصل بـ ---)")
    parser.add_argument("--business", default="", help="نوع النشاط التجاري")
    parser.add_argument("--language", default="ar", help="اللغة (ar/en)")
    parser.add_argument("--save", action="store_true", help="حفظ النتيجة في ملف")
    args = parser.parse_args()

    gen = FeedbackAnalyzer()
    if args.save:
        path = gen.generate_and_save(args.feedback, business=args.business, language=args.language)
        print(f"تم الحفظ في: {path}")
    else:
        print(gen.analyze(args.feedback, business=args.business, language=args.language))


if __name__ == "__main__":
    main()
