"""AI Grant Proposal Writer - Winning grant applications.
Usage: python -m income_streams.grant_proposals.writer --project "مشروع تقني" --amount 500000
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class GrantProposalWriter:
    def __init__(self):
        self.client = AIClient()

    def generate(self, project, funder="", amount=0, duration="12 months", language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"كاتب مقترحات منح محترف بنسبة نجاح عالية بـ{lang}. "
            "تكتب مقترحات مقنعة تتبع معايير الممولين. تعرف صناديق الدعم السعودية (منشآت، صندوق التنمية، إلخ)."
        )
        prompt = f"""اكتب مقترح منحة/تمويل:
المشروع: {project}
{"الممول: " + funder if funder else "ممول عام"}
{"المبلغ المطلوب: " + str(amount) + " ريال" if amount else ""}
المدة: {duration}

أعطني مقترح كامل يشمل:
1. ملخص تنفيذي
2. وصف المشروع والمشكلة التي يحلها
3. الأهداف (SMART)
4. المنهجية وخطة التنفيذ
5. الجدول الزمني
6. الميزانية التفصيلية
7. فريق العمل المطلوب
8. الأثر المتوقع (اجتماعي/اقتصادي)
9. خطة الاستدامة
10. مؤشرات النجاح (KPIs)"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, project, **kw):
        content = self.generate(project, **kw)
        return save_output(content, timestamp_filename(f"grant_{project}", "md"), str(get_output_dir("reports")))

def main():
    parser = argparse.ArgumentParser(description="Grant Proposal Writer - كاتب مقترحات المنح")
    parser.add_argument("--project", "-p", required=True)
    parser.add_argument("--funder", "-f", default="")
    parser.add_argument("--amount", "-a", type=float, default=0)
    parser.add_argument("--duration", "-d", default="12 months")
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    writer = GrantProposalWriter()
    if args.save:
        print(f"Saved to: {writer.generate_and_save(args.project, funder=args.funder, amount=args.amount, duration=args.duration)}")
    else:
        print(writer.generate(args.project, args.funder, args.amount, args.duration))

if __name__ == "__main__":
    main()
