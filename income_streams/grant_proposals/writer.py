"""AI Grant Proposal Writer - Income Stream #49.
Business Model: كتابة مقترحات المنح بالذكاء الاصطناعي
Usage: python -m income_streams.grant_proposals.writer --project "منصة تعليمية رقمية" --funder "منشآت" --amount 500000 --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class GrantProposalWriter:
    def __init__(self):
        self.client = AIClient(module_name="grant_proposals")

    def generate(self, project: str, funder: str = "", amount: float = 0, duration: str = "12 months", language: str = "ar") -> str:
        system = (
            "كاتب مقترحات منح محترف بنسبة نجاح عالية. "
            "يكتب مقترحات مقنعة تتبع معايير الممولين الرئيسيين (حكومي، خاص، دولي). "
            "يعرف صناديق الدعم السعودية (منشآت، صندوق التنمية الصناعية، صندوق التنمية الزراعية، "
            "بنك التنمية الاجتماعية، مسك الخيرية، إلخ). "
            "يفهم معايير التقييم ويعرف كيف يكتب مقترحاً يحصل على أعلى الدرجات. "
            "خبير في الميزانيات التفصيلية والجداول الزمنية ومؤشرات الأداء."
        )
        lang_instruction = "قدم المحتوى باللغة العربية مع المصطلحات الإنجليزية عند الحاجة." if language == "ar" else "Present content in English."
        funder_section = f"\nالجهة الممولة: {funder}" if funder else "\nالجهة الممولة: غير محددة (اقترح جهات مناسبة)"
        amount_section = f"\nالمبلغ المطلوب: {amount:,.0f} ريال" if amount > 0 else "\nالمبلغ: غير محدد (اقترح ميزانية مناسبة)"
        prompt = (
            f"اكتب مقترح منحة/تمويل احترافي:\n"
            f"المشروع: {project}\n"
            f"{funder_section}\n"
            f"{amount_section}\n"
            f"المدة: {duration}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. الملخص التنفيذي (Executive Summary)\n"
            f"- وصف المشروع في فقرة واحدة مقنعة\n"
            f"- المشكلة والحل\n"
            f"- المبلغ المطلوب والعائد المتوقع\n\n"
            f"## 2. وصف المشروع\n"
            f"- خلفية المشروع\n"
            f"- المشكلة التي يحلها\n"
            f"- الحل المقترح\n"
            f"- الفئة المستهدفة\n"
            f"- القيمة المضافة\n\n"
            f"## 3. الأهداف\n"
            f"- الهدف العام\n"
            f"- الأهداف التفصيلية (SMART)\n"
            f"- المخرجات المتوقعة\n\n"
            f"## 4. المنهجية وخطة العمل\n"
            f"- مراحل التنفيذ\n"
            f"- الأنشطة الرئيسية\n"
            f"- الأدوات والتقنيات\n\n"
            f"## 5. الجدول الزمني\n"
            f"- مخطط جانت مبسط\n"
            f"- المراحل والمعالم الرئيسية (Milestones)\n"
            f"- التسليمات لكل مرحلة\n\n"
            f"## 6. الميزانية التفصيلية\n"
            f"- جدول الميزانية (البند، الوحدة، العدد، التكلفة)\n"
            f"- تكاليف الموارد البشرية\n"
            f"- تكاليف التشغيل\n"
            f"- تكاليف التسويق\n"
            f"- احتياطي الطوارئ (10%)\n\n"
            f"## 7. فريق العمل\n"
            f"- الهيكل التنظيمي المقترح\n"
            f"- الأدوار والمسؤوليات\n"
            f"- المؤهلات المطلوبة\n\n"
            f"## 8. الأثر المتوقع\n"
            f"- الأثر الاقتصادي\n"
            f"- الأثر الاجتماعي\n"
            f"- الأثر على رؤية 2030\n\n"
            f"## 9. الاستدامة\n"
            f"- خطة الاستدامة بعد انتهاء المنحة\n"
            f"- مصادر الدخل المستقبلية\n"
            f"- استراتيجية التوسع\n\n"
            f"## 10. مؤشرات النجاح (KPIs)\n"
            f"- مؤشرات كمية ونوعية\n"
            f"- آلية القياس والتقييم\n"
            f"- التقارير الدورية\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_budget_justification(self, project: str, amount: float) -> str:
        system = (
            "خبير مالي متخصص في إعداد ميزانيات المشاريع وتبريرها. "
            "يعرف معايير الممولين في قبول بنود الميزانية."
        )
        prompt = (
            f"أعد تبرير ميزانية مفصل للمشروع التالي:\n"
            f"المشروع: {project}\n"
            f"المبلغ الإجمالي: {amount:,.0f} ريال\n\n"
            f"قدم:\n"
            f"- توزيع الميزانية على البنود الرئيسية (مع النسب)\n"
            f"- تبرير كل بند (لماذا هذا المبلغ)\n"
            f"- مقارنة بأسعار السوق\n"
            f"- خطة صرف شهرية/ربعية\n"
            f"- آلية الرقابة المالية\n"
            f"- البدائل في حالة تخفيض الميزانية\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_and_save(self, project: str, **kw) -> str:
        content = self.generate(project, **kw)
        return save_output(content, timestamp_filename("grant_proposal", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Grant Proposal Writer - كتابة مقترحات منح بالذكاء الاصطناعي")
    parser.add_argument("--project", required=True, help="وصف المشروع")
    parser.add_argument("--funder", default="", help="الجهة الممولة")
    parser.add_argument("--amount", type=float, default=0, help="المبلغ المطلوب بالريال")
    parser.add_argument("--duration", default="12 months", help="مدة المشروع")
    parser.add_argument("--language", default="ar", help="اللغة (ar/en)")
    parser.add_argument("--save", action="store_true", help="حفظ النتيجة في ملف")
    args = parser.parse_args()

    gen = GrantProposalWriter()
    if args.save:
        path = gen.generate_and_save(args.project, funder=args.funder, amount=args.amount, duration=args.duration, language=args.language)
        print(f"تم الحفظ في: {path}")
    else:
        print(gen.generate(args.project, funder=args.funder, amount=args.amount, duration=args.duration, language=args.language))


if __name__ == "__main__":
    main()
