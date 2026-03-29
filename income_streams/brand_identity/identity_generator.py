"""AI Brand Identity Generator - Income Stream #20.
Business Model: تصميم هوية العلامة التجارية بالذكاء الاصطناعي (500-3,000 ريال/هوية)
Usage: python -m income_streams.brand_identity.identity_generator --business "وصف النشاط" --style modern --values "ابتكار,جودة" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class BrandIdentityGenerator:
    def __init__(self):
        self.client = AIClient(module_name="brand_identity")

    def generate(self, business_description: str, style: str = "modern", values: str = "", language: str = "ar") -> str:
        system = (
            "أنت مصمم هوية بصرية وخبير علامات تجارية بخبرة تزيد عن 10 سنوات في تصميم هويات تجارية متكاملة للسوق السعودي والخليجي. "
            "عملت مع شركات ناشئة وعلامات تجارية كبرى في مختلف القطاعات. "
            "تفهم علم نفس الألوان وتأثيرها على الجمهور العربي، وتختار الخطوط العربية والإنجليزية بعناية. "
            "تصمم هويات تجارية تعكس القيم والثقافة المحلية مع لمسة عصرية عالمية. "
            "تلتزم بمعايير التصميم الاحترافي وتقدم دليل هوية شامل قابل للتطبيق الفوري."
        )
        lang_instruction = "قدم المحتوى باللغة العربية مع المصطلحات الإنجليزية عند الحاجة." if language == "ar" else "Present in English with Arabic brand name suggestions."
        style_map = {
            "modern": "عصري وحديث: خطوط نظيفة، ألوان جريئة، تصميم بسيط ومؤثر",
            "classic": "كلاسيكي وراقي: ألوان داكنة، خطوط serif، تفاصيل فاخرة",
            "playful": "مرح وحيوي: ألوان زاهية، خطوط مستديرة، عناصر ممتعة",
            "luxury": "فاخر وحصري: ذهبي/أسود، خطوط رفيعة، تصميم أنيق ومميز",
            "minimal": "بسيط ونظيف: ألوان محدودة، مساحات بيضاء، أقل هو أكثر"
        }
        style_desc = style_map.get(style, style_map["modern"])
        values_section = f"\nالقيم الأساسية: {values}" if values else ""
        prompt = (
            f"صمم هوية تجارية متكاملة للنشاط التالي:\n{business_description}\n"
            f"النمط المطلوب: {style_desc}\n"
            f"{values_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي بالتفصيل:\n\n"
            f"## 1. اقتراحات الأسماء (5 خيارات)\n"
            f"لكل اسم: الاسم بالعربي + الاسم بالإنجليزي + المعنى + سبب الاختيار + توفر النطاق (.com/.sa)\n\n"
            f"## 2. الشعار (Logo)\n"
            f"- وصف تفصيلي لتصميم الشعار (الشكل، العناصر، الرمزية)\n"
            f"- النسخة الرئيسية والنسخة المبسطة والأيقونة\n"
            f"- قواعد الاستخدام (المساحات، الحد الأدنى للحجم)\n\n"
            f"## 3. لوحة الألوان (6 ألوان)\n"
            f"لكل لون: الاسم + كود HEX + كود RGB + الاستخدام + التأثير النفسي\n"
            f"- اللون الأساسي (Primary)\n"
            f"- اللون الثانوي (Secondary)\n"
            f"- لون التمييز (Accent)\n"
            f"- 3 ألوان مساعدة (خلفية، نص، محايد)\n\n"
            f"## 4. الخطوط المقترحة\n"
            f"- خط العناوين العربي + الإنجليزي\n"
            f"- خط النصوص العربي + الإنجليزي\n"
            f"- أحجام الخطوط المقترحة\n\n"
            f"## 5. نبرة العلامة (Brand Voice)\n"
            f"- الشخصية (5 صفات)\n"
            f"- أسلوب الكتابة (أمثلة نعم/لا)\n"
            f"- نبرة التواصل على كل منصة\n\n"
            f"## 6. الرسالة والرؤية والقيم\n"
            f"- الرسالة (Mission)\n"
            f"- الرؤية (Vision)\n"
            f"- القيم (5 قيم مع شرح)\n"
            f"- الشعار النصي (Tagline) - 3 خيارات\n\n"
            f"## 7. دليل استخدام الشعار\n"
            f"- الاستخدامات الصحيحة والخاطئة\n"
            f"- الخلفيات المسموحة\n"
            f"- المساحات الآمنة\n\n"
            f"## 8. التطبيقات\n"
            f"- بطاقة أعمال (وصف التصميم للوجهين)\n"
            f"- ورق رسمي (Letterhead)\n"
            f"- قوالب سوشال ميديا (إنستغرام، تويتر، لينكدإن)\n"
            f"- توقيع البريد الإلكتروني\n"
            f"- غلاف الموقع الإلكتروني"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_naming(self, business_type: str, attributes: str) -> str:
        system = (
            "أنت خبير تسمية علامات تجارية (Brand Naming) متخصص في السوق العربي والخليجي. "
            "تبتكر أسماء تجارية سهلة النطق والتذكر بالعربي والإنجليزي مع التأكد من ملاءمتها الثقافية."
        )
        prompt = (
            f"ابتكر أسماء تجارية لـ: {business_type}\n"
            f"الصفات المطلوبة: {attributes}\n\n"
            f"قدم 10 اقتراحات، لكل واحد:\n"
            f"1. الاسم بالعربي والإنجليزي\n"
            f"2. المعنى والدلالة\n"
            f"3. سهولة النطق (تقييم 1-10)\n"
            f"4. قابلية التذكر (تقييم 1-10)\n"
            f"5. توفر النطاق المتوقع\n"
            f"6. توفر حسابات السوشال ميديا\n"
            f"7. الملاءمة الثقافية\n"
            f"8. اقتراح أولي للشعار"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_brand_guide(self, brand_name: str, industry: str) -> str:
        system = (
            "أنت مستشار علامات تجارية خبير في إعداد أدلة العلامة التجارية (Brand Guidelines) الشاملة. "
            "تصمم أدلة احترافية تضمن اتساق العلامة عبر جميع نقاط التواصل."
        )
        prompt = (
            f"أنشئ دليل علامة تجارية شامل لـ: {brand_name}\n"
            f"القطاع: {industry}\n\n"
            f"المطلوب:\n"
            f"1. **قصة العلامة** (Brand Story)\n"
            f"2. **الهوية البصرية** (الشعار، الألوان، الخطوط)\n"
            f"3. **نبرة التواصل** (Brand Voice & Tone)\n"
            f"4. **دليل المحتوى** (Content Guidelines)\n"
            f"5. **دليل السوشال ميديا** (قوالب، أسلوب، تكرار النشر)\n"
            f"6. **دليل التصوير** (Photography Style)\n"
            f"7. **الأيقونات والرسوم** (Iconography)\n"
            f"8. **التطبيقات المطبوعة والرقمية**\n"
            f"9. **الأخطاء الشائعة** (ما يجب تجنبه)\n"
            f"10. **قائمة مراجعة الاتساق** (Consistency Checklist)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, business_description: str, **kwargs) -> str:
        content = self.generate(business_description, **kwargs)
        return save_output(content, timestamp_filename("brand_identity", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Brand Identity Generator - مولد الهوية التجارية بالذكاء الاصطناعي")
    parser.add_argument("--business", "-b", required=True, help="وصف النشاط التجاري")
    parser.add_argument("--style", choices=["modern", "classic", "playful", "luxury", "minimal"], default="modern", help="نمط الهوية")
    parser.add_argument("--values", "-v", default="", help="القيم الأساسية (مفصولة بفواصل)")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = BrandIdentityGenerator()
    if args.save:
        path = gen.generate_and_save(args.business, style=args.style, values=args.values, language=args.language)
        print(f"Saved to: {path}")
    else:
        print(gen.generate(args.business, style=args.style, values=args.values, language=args.language))


if __name__ == "__main__":
    main()
