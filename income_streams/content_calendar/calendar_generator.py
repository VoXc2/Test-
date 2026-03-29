"""AI Content Calendar Generator - 30-day content plans.
Usage: python -m income_streams.content_calendar.calendar_generator --brand "متجر أزياء" --platforms "insta,twitter"
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class ContentCalendarGenerator:
    def __init__(self):
        self.client = AIClient()

    def generate(self, brand, platforms, month="", num_days=30, language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"مدير محتوى محترف ومخطط سوشال ميديا بـ{lang}. "
            "تصمم تقويمات محتوى استراتيجية تراعي المناسبات المحلية السعودية والعالمية."
        )
        prompt = f"""أنشئ تقويم محتوى {num_days} يوم:
العلامة التجارية: {brand}
المنصات: {platforms}
{"الشهر: " + month if month else "الشهر القادم"}

لكل يوم أعطني:
- المنصة
- نوع المحتوى (صورة/فيديو/ريلز/كاروسيل/ستوري/نص)
- فكرة المحتوى (جملة واحدة)
- الوقت المقترح للنشر
- الهاشتاقات

أيضاً أضف:
- المناسبات الخاصة في الشهر
- مؤشرات الأداء المستهدفة
- أسبوع نموذجي مفصل (المحتوى كامل)"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, brand, **kw):
        content = self.generate(brand, **kw)
        return save_output(content, timestamp_filename(f"calendar_{brand}", "md"), str(get_output_dir("content")))

def main():
    parser = argparse.ArgumentParser(description="Content Calendar - تقويم المحتوى")
    parser.add_argument("--brand", "-b", required=True)
    parser.add_argument("--platforms", "-p", required=True, help="Comma-separated: insta,twitter,tiktok")
    parser.add_argument("--month", "-m", default="")
    parser.add_argument("--days", "-d", type=int, default=30)
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    gen = ContentCalendarGenerator()
    if args.save:
        print(f"Saved to: {gen.generate_and_save(args.brand, platforms=args.platforms, month=args.month, num_days=args.days)}")
    else:
        print(gen.generate(args.brand, args.platforms, args.month, args.days))

if __name__ == "__main__":
    main()
