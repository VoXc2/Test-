"""AI Infographic Content Generator - Income Stream #21.
Business Model: إنشاء محتوى إنفوجرافيك بالذكاء الاصطناعي (50-200 ريال/إنفوجرافيك)
Usage: python -m income_streams.infographic_engine.infographic_generator --topic "الموضوع" --style data_driven --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class InfographicGenerator:
    def __init__(self):
        self.client = AIClient(module_name="infographic_engine")

    def generate(self, topic: str, style: str = "data_driven", language: str = "ar") -> str:
        system = (
            "أنت مصمم إنفوجرافيك محترف وخبير تصور بيانات بخبرة تزيد عن 8 سنوات. "
            "تكتب محتوى إنفوجرافيك منظم وجذاب جاهز للتصميم في Canva أو Figma أو أي أداة تصميم. "
            "تفهم مبادئ التصور المرئي للبيانات وقواعد التصميم المعلوماتي (Information Design). "
            "تعرف كيف تحوّل البيانات المعقدة إلى رسوم بصرية بسيطة وجذابة يفهمها الجميع. "
            "تراعي اتجاه القراءة العربية (من اليمين لليسار) وتختار الألوان والخطوط المناسبة للجمهور العربي. "
            "تلتزم بمبدأ البساطة: كل عنصر بصري يجب أن يخدم هدفًا واضحًا."
        )
        lang_instruction = "اكتب المحتوى باللغة العربية." if language == "ar" else "Write the content in English."
        style_map = {
            "data_driven": "إنفوجرافيك مبني على البيانات والإحصائيات مع رسوم بيانية",
            "comparison": "إنفوجرافيك مقارنة بين عنصرين أو أكثر",
            "process": "إنفوجرافيك عملية/خطوات متسلسلة",
            "timeline": "إنفوجرافيك خط زمني (تاريخي أو مستقبلي)",
            "list": "إنفوجرافيك قائمة (نصائح، حقائق، معلومات)"
        }
        style_desc = style_map.get(style, style_map["data_driven"])
        prompt = (
            f"أنشئ محتوى إنفوجرافيك جاهز للتصميم عن: {topic}\n"
            f"النوع: {style_desc}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي بالتفصيل:\n\n"
            f"## 1. العنوان الرئيسي\n"
            f"- عنوان جذاب وقصير (5-8 كلمات)\n"
            f"- 3 خيارات للعنوان\n\n"
            f"## 2. العنوان الفرعي\n"
            f"- جملة توضيحية (10-15 كلمة)\n\n"
            f"## 3. الأقسام (3-6 أقسام)\n"
            f"لكل قسم:\n"
            f"- عنوان القسم\n"
            f"- البيانات/الإحصائيات الرئيسية (أرقام بارزة)\n"
            f"- النص التوضيحي (جملة أو جملتان)\n"
            f"- نوع الرسم البياني المقترح (دائري/أعمدة/خطي/أيقونات)\n\n"
            f"## 4. الأيقونات المقترحة\n"
            f"- أيقونة لكل قسم مع وصفها\n"
            f"- مكتبات أيقونات مقترحة (Flaticon, Font Awesome)\n\n"
            f"## 5. الألوان المقترحة\n"
            f"- لوحة ألوان (4-5 ألوان مع أكواد HEX)\n"
            f"- اللون الرئيسي والثانوي ولون التمييز\n"
            f"- سبب اختيار كل لون\n\n"
            f"## 6. الخلاصة\n"
            f"- جملة ختامية مؤثرة أو CTA\n"
            f"- رقم/إحصائية بارزة للختام\n\n"
            f"## 7. المصادر\n"
            f"- مصادر البيانات والإحصائيات\n\n"
            f"## 8. الحجم المقترح\n"
            f"- الأبعاد المثالية (بكسل) حسب منصة النشر\n"
            f"- نسخة إنستغرام (1080x1080 أو 1080x1350)\n"
            f"- نسخة تويتر (1200x675)\n"
            f"- نسخة Pinterest (1000x2100)\n\n"
            f"## 9. تعليمات التصميم\n"
            f"- اتجاه القراءة وتدفق المعلومات\n"
            f"- التسلسل الهرمي البصري\n"
            f"- الخطوط المقترحة (عربي + انجليزي)\n"
            f"- المساحات البيضاء والهوامش\n"
            f"- نصائح لجعل الإنفوجرافيك قابل للمشاركة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_comparison(self, item1: str, item2: str) -> str:
        system = (
            "أنت خبير تصور بيانات متخصص في إنفوجرافيك المقارنات. "
            "تصمم مقارنات بصرية واضحة وعادلة تساعد القارئ على اتخاذ قرار مبني على معلومات دقيقة. "
            "تستخدم تقنيات بصرية فعالة: الأعمدة المتقابلة، الرموز، والألوان المتباينة."
        )
        prompt = (
            f"أنشئ محتوى إنفوجرافيك مقارنة بين:\n"
            f"العنصر الأول: {item1}\n"
            f"العنصر الثاني: {item2}\n\n"
            f"المطلوب:\n"
            f"1. **العنوان**: مقارنة جذابة\n"
            f"2. **معايير المقارنة** (6-10 معايير)\n"
            f"   لكل معيار: القيمة لكل عنصر + أيقونة + رسم بياني مقترح\n"
            f"3. **الملخص**: أيهما أفضل ولماذا (حسب السياق)\n"
            f"4. **نصيحة الخبير**: متى تختار كل واحد\n"
            f"5. **الألوان**: لون مميز لكل عنصر (مع HEX)\n"
            f"6. **تعليمات التصميم**: تخطيط الأعمدة المتقابلة\n"
            f"7. **الحجم والأبعاد المقترحة**"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_process(self, process_name: str, steps: int = 0) -> str:
        system = (
            "أنت خبير تصور عمليات ومصمم إنفوجرافيك خطوات متسلسلة. "
            "تحوّل العمليات المعقدة إلى خطوات بصرية واضحة ومتسلسلة يسهل اتباعها. "
            "تستخدم الأسهم والأرقام والأيقونات لتوضيح التدفق والتسلسل."
        )
        steps_instruction = f"عدد الخطوات المطلوب: {steps}" if steps > 0 else "حدد عدد الخطوات المناسب (5-10 خطوات)"
        prompt = (
            f"أنشئ محتوى إنفوجرافيك خطوات/عملية لـ: {process_name}\n"
            f"{steps_instruction}\n\n"
            f"المطلوب:\n"
            f"1. **العنوان**: عنوان واضح وجذاب\n"
            f"2. **المقدمة**: لماذا هذه العملية مهمة (جملة واحدة)\n"
            f"3. **الخطوات**: لكل خطوة:\n"
            f"   - الرقم والعنوان\n"
            f"   - الشرح المختصر (جملة واحدة)\n"
            f"   - الأيقونة المقترحة\n"
            f"   - نصيحة سريعة (Tip)\n"
            f"   - الربط بالخطوة التالية\n"
            f"4. **النتيجة النهائية**: ماذا تحقق بعد إتمام الخطوات\n"
            f"5. **التصميم**: تدفق عمودي أو أفقي أو دائري\n"
            f"6. **الألوان والأيقونات**\n"
            f"7. **الأبعاد المقترحة**"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        content = self.generate(topic, **kwargs)
        return save_output(content, timestamp_filename("infographic", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Infographic Generator - مولد الإنفوجرافيك بالذكاء الاصطناعي")
    parser.add_argument("--topic", "-t", required=True, help="موضوع الإنفوجرافيك")
    parser.add_argument("--style", choices=["data_driven", "comparison", "process", "timeline", "list"], default="data_driven", help="نمط الإنفوجرافيك")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="اللغة")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = InfographicGenerator()
    if args.save:
        path = gen.generate_and_save(args.topic, style=args.style, language=args.language)
        print(f"Saved to: {path}")
    else:
        print(gen.generate(args.topic, style=args.style, language=args.language))


if __name__ == "__main__":
    main()
