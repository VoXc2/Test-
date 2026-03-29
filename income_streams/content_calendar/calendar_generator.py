"""AI Content Calendar Generator - Income Stream #46.
Business Model: إنشاء تقويمات محتوى بالذكاء الاصطناعي
Usage: python -m income_streams.content_calendar.calendar_generator --brand "متجر إلكتروني" --platforms "instagram,twitter,tiktok" --days 30 --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class ContentCalendarGenerator:
    def __init__(self):
        self.client = AIClient(module_name="content_calendar")

    def generate(self, brand: str, platforms: str, month: str = "", num_days: int = 30, language: str = "ar") -> str:
        system = (
            "مدير محتوى محترف ومخطط سوشال ميديا. "
            "يصمم تقويمات محتوى استراتيجية تتضمن أنواع مختلفة من المحتوى وتراعي المناسبات المحلية والعالمية. "
            "يفهم خوارزميات كل منصة ويعرف أفضل الأوقات والأنواع لكل منها. "
            "يراعي التوازن بين المحتوى التعليمي والترفيهي والترويجي. "
            "يعرف المناسبات السعودية والخليجية والإسلامية ويدمجها في الخطة."
        )
        lang_instruction = "قدم المحتوى باللغة العربية." if language == "ar" else "Present content in English."
        month_section = f"\nالشهر: {month}" if month else ""
        platform_list = [p.strip() for p in platforms.split(",")]
        platforms_formatted = "، ".join(platform_list)
        prompt = (
            f"أنشئ تقويم محتوى شامل:\n"
            f"العلامة التجارية/النشاط: {brand}\n"
            f"المنصات: {platforms_formatted}\n"
            f"عدد الأيام: {num_days}\n"
            f"{month_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. الاستراتيجية العامة\n"
            f"- أهداف المحتوى لهذه الفترة\n"
            f"- توزيع أنواع المحتوى (تعليمي 40% / ترفيهي 30% / ترويجي 20% / تفاعلي 10%)\n"
            f"- نبرة المحتوى على كل منصة\n\n"
            f"## 2. تقويم {num_days} يوم\n"
            f"لكل يوم:\n"
            f"| اليوم | التاريخ | المنصة | نوع المحتوى | فكرة المحتوى | الوقت المقترح | الهاشتاقات | ملاحظات |\n\n"
            f"## 3. المناسبات الخاصة\n"
            f"- مناسبات وطنية ودينية خلال الفترة\n"
            f"- أيام عالمية مناسبة للنشاط\n"
            f"- أفكار محتوى خاصة لكل مناسبة\n\n"
            f"## 4. مؤشرات الأداء (KPIs)\n"
            f"- الأهداف الرقمية لكل منصة\n"
            f"- مقاييس النجاح الأسبوعية\n"
            f"- أدوات القياس المقترحة\n\n"
            f"## 5. أسبوع نموذجي مفصل\n"
            f"- تفاصيل كاملة لأسبوع واحد (كل منشور بالتفصيل)\n"
            f"- النص الكامل لكل منشور\n"
            f"- التصميم المقترح\n"
            f"- الهاشتاقات الكاملة\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_weekly(self, brand: str, platforms: str, theme: str = "") -> str:
        system = (
            "مدير محتوى محترف ومخطط سوشال ميديا. "
            "يصمم خطط أسبوعية مفصلة وجاهزة للتنفيذ."
        )
        theme_section = f"\nالثيم/الموضوع: {theme}" if theme else ""
        platform_list = [p.strip() for p in platforms.split(",")]
        platforms_formatted = "، ".join(platform_list)
        prompt = (
            f"أنشئ خطة محتوى أسبوعية مفصلة وجاهزة للتنفيذ:\n"
            f"العلامة التجارية: {brand}\n"
            f"المنصات: {platforms_formatted}\n"
            f"{theme_section}\n\n"
            f"لكل يوم من الأسبوع، قدم لكل منصة:\n"
            f"- فكرة المحتوى الكاملة\n"
            f"- النص الجاهز للنشر (Caption)\n"
            f"- وصف التصميم/الفيديو\n"
            f"- الهاشتاقات\n"
            f"- وقت النشر الأمثل\n"
            f"- CTA المناسب\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, brand: str, platforms: str, **kw) -> str:
        content = self.generate(brand, platforms, **kw)
        return save_output(content, timestamp_filename("content_calendar", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Content Calendar Generator - تقويم محتوى بالذكاء الاصطناعي")
    parser.add_argument("--brand", required=True, help="اسم العلامة التجارية أو النشاط")
    parser.add_argument("--platforms", required=True, help="المنصات (مفصولة بفواصل: instagram,twitter,tiktok)")
    parser.add_argument("--month", default="", help="الشهر المستهدف")
    parser.add_argument("--days", type=int, default=30, help="عدد الأيام")
    parser.add_argument("--language", default="ar", help="اللغة (ar/en)")
    parser.add_argument("--save", action="store_true", help="حفظ النتيجة في ملف")
    args = parser.parse_args()

    gen = ContentCalendarGenerator()
    if args.save:
        path = gen.generate_and_save(args.brand, args.platforms, month=args.month, num_days=args.days, language=args.language)
        print(f"تم الحفظ في: {path}")
    else:
        print(gen.generate(args.brand, args.platforms, month=args.month, num_days=args.days, language=args.language))


if __name__ == "__main__":
    main()
