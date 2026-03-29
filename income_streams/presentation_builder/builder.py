"""AI Presentation Builder - Income Stream #17.
Business Model: بناء عروض تقديمية احترافية بالذكاء الاصطناعي (100-500 ريال/عرض)
Usage: python -m income_streams.presentation_builder.builder --topic "الموضوع" --slides 15 --style professional --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class PresentationBuilder:
    def __init__(self):
        self.client = AIClient(module_name="presentation_builder")

    def generate(self, topic: str, slides: int = 15, style: str = "professional", language: str = "ar") -> str:
        system = (
            "أنت خبير عروض تقديمية ومستشار اتصالات مؤسسية بخبرة تزيد عن 15 عامًا في تصميم العروض للشركات الكبرى والمؤتمرات الدولية. "
            "تصمم عروض مقنعة تتبع مبادئ التصميم الاحترافي وعلم النفس الإقناعي المبني على أبحاث علمية. "
            "تكتب محتوى كل شريحة بدقة مع ملاحظات المتحدث التفصيلية واقتراحات بصرية عملية قابلة للتنفيذ. "
            "تراعي تسلسل الأفكار المنطقي وتدرج المعلومات من العام إلى الخاص. "
            "تلتزم بقاعدة 6x6 (لا أكثر من 6 نقاط في الشريحة، لا أكثر من 6 كلمات في النقطة). "
            "تفهم الفرق بين أنماط العروض: الاحترافي للشركات، الإبداعي للتسويق، والمبسط للتعليم."
        )
        lang_instruction = "اكتب العرض باللغة العربية." if language == "ar" else "Write the presentation in English."
        style_map = {
            "professional": "النمط الاحترافي المؤسسي: ألوان هادئة، خطوط رسمية، تصميم نظيف ومنظم",
            "creative": "النمط الإبداعي: ألوان جريئة، تصاميم غير تقليدية، عناصر بصرية ملفتة",
            "minimal": "النمط المبسط: خلفيات بيضاء، نص محدود جدًا، تركيز على الصور والرسوم"
        }
        style_desc = style_map.get(style, style_map["professional"])
        prompt = (
            f"أنشئ عرضًا تقديميًا احترافيًا عن: {topic}\n"
            f"عدد الشرائح: {slides}\n"
            f"النمط: {style_desc}\n"
            f"{lang_instruction}\n\n"
            f"لكل شريحة قدّم التالي بالتفصيل:\n"
            f"1. **رقم الشريحة وعنوانها**\n"
            f"2. **المحتوى الرئيسي**: النقاط والنصوص (التزم بقاعدة 6x6)\n"
            f"3. **ملاحظات المتحدث**: ما يقوله المقدم بالتفصيل (3-5 جمل)\n"
            f"4. **الاقتراح البصري**: نوع العنصر البصري (رسم بياني/صورة/جدول/أيقونات) مع وصف تفصيلي\n"
            f"5. **الانتقال**: كيفية الربط بالشريحة التالية\n\n"
            f"ابدأ بشريحة العنوان واختم بشريحة الأسئلة والتواصل.\n"
            f"أضف في النهاية:\n"
            f"- ملخص لوحة الألوان المقترحة (مع أكواد HEX)\n"
            f"- الخطوط المقترحة (عربي وانجليزي)\n"
            f"- نصائح لتقديم العرض بفعالية\n"
            f"- الوقت المقترح لكل شريحة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_pitch_deck(self, startup_info: str) -> str:
        system = (
            "أنت خبير في إعداد عروض Pitch Deck للشركات الناشئة مع خبرة في مسرعات الأعمال وجمع التمويل. "
            "تصمم عروض استثمارية مقنعة تتبع هيكل Guy Kawasaki (10 شرائح) مع تعديلات للسوق السعودي والخليجي. "
            "تفهم ما يبحث عنه المستثمرون وصناديق رأس المال الجريء في المنطقة."
        )
        prompt = (
            f"أنشئ Pitch Deck احترافي للشركة الناشئة التالية:\n{startup_info}\n\n"
            f"الهيكل المطلوب (10-12 شريحة):\n"
            f"1. شريحة العنوان (الاسم، الشعار، Tagline)\n"
            f"2. المشكلة (بيانات وإحصائيات)\n"
            f"3. الحل (كيف نحل المشكلة)\n"
            f"4. نموذج العمل (كيف نربح)\n"
            f"5. السوق المستهدف (TAM, SAM, SOM)\n"
            f"6. المنافسة (مصفوفة المقارنة)\n"
            f"7. الجذب/الإنجازات (Traction)\n"
            f"8. الفريق (الخبرات والمؤهلات)\n"
            f"9. الخطة المالية (التوقعات لـ3 سنوات)\n"
            f"10. الطلب (المبلغ المطلوب واستخدامه)\n\n"
            f"لكل شريحة: المحتوى + ملاحظات المتحدث + الاقتراح البصري"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        content = self.generate(topic, **kwargs)
        return save_output(content, timestamp_filename("presentation", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Presentation Builder - بناء العروض التقديمية بالذكاء الاصطناعي")
    parser.add_argument("--topic", "-t", required=True, help="موضوع العرض التقديمي")
    parser.add_argument("--slides", "-n", type=int, default=15, help="عدد الشرائح (افتراضي: 15)")
    parser.add_argument("--style", choices=["professional", "creative", "minimal"], default="professional", help="نمط العرض")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="لغة العرض")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = PresentationBuilder()
    if args.save:
        path = gen.generate_and_save(args.topic, slides=args.slides, style=args.style, language=args.language)
        print(f"Saved to: {path}")
    else:
        print(gen.generate(args.topic, slides=args.slides, style=args.style, language=args.language))


if __name__ == "__main__":
    main()
