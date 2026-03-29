"""AI Landing Page Copy Generator - Income Stream #53.
Business Model: كتابة نصوص صفحات الهبوط بالذكاء الاصطناعي (400-2,500 ريال/صفحة)
Usage: python -m income_streams.landing_page_copy.copy_generator --product "وصف المنتج" --type sales --tone professional --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class LandingPageCopyGenerator:
    def __init__(self):
        self.client = AIClient(module_name="landing_page_copy")

    def generate(self, product: str, page_type: str = "sales", tone: str = "professional", language: str = "ar") -> str:
        system = (
            "أنت كاتب نصوص تحويلية (Conversion Copywriter) محترف متدرب على أقوى أطر الكتابة الإقناعية: "
            "PAS (Problem-Agitation-Solution)، AIDA (Attention-Interest-Desire-Action)، وإطار StoryBrand. "
            "كتبت نصوص صفحات هبوط حققت معدلات تحويل تتجاوز 15% في السوق العربي والخليجي. "
            "تفهم سيكولوجية الإقناع والتأثير وتطبق مبادئ روبرت تشالديني الستة في كل نص تكتبه. "
            "تكتب عناوين تجذب الانتباه خلال 3 ثوانٍ ونصوص تبني الرغبة وتحفز الفعل الفوري. "
            "تتقن الكتابة للسوق العربي مع مراعاة الخصوصيات الثقافية والدينية والاجتماعية."
        )
        lang_instruction = "اكتب جميع النصوص باللغة العربية الفصحى المبسطة مع قوة التأثير." if language == "ar" else "Write all copy in English optimized for MENA market audience."
        type_map = {
            "sales": "صفحة مبيعات: صفحة طويلة مقنعة لبيع منتج/خدمة مباشرة",
            "squeeze": "صفحة التقاط بيانات (Squeeze Page): صفحة قصيرة لجمع البريد الإلكتروني مقابل هدية مجانية",
            "webinar": "صفحة تسجيل ندوة (Webinar Registration): صفحة لإقناع الزائر بالتسجيل في ندوة مباشرة",
            "coming_soon": "صفحة قريبًا (Coming Soon): صفحة لبناء الترقب وجمع قائمة الانتظار",
            "product": "صفحة منتج (Product Page): صفحة عرض منتج بتفاصيله ومزاياه"
        }
        type_desc = type_map.get(page_type, type_map["sales"])
        tone_map = {
            "professional": "احترافي ورسمي: لغة واثقة ومصداقية عالية",
            "casual": "ودّي وغير رسمي: لغة قريبة وشخصية كأنك تتحدث مع صديق",
            "urgent": "عاجل ومُلح: لغة تحفز الفعل الفوري مع عناصر الندرة والوقت المحدود",
            "luxury": "فاخر وحصري: لغة راقية تستهدف الشريحة العليا مع إحساس بالتميز"
        }
        tone_desc = tone_map.get(tone, tone_map["professional"])
        prompt = (
            f"اكتب نص صفحة هبوط كامل ومقنع للمنتج/الخدمة التالية:\n{product}\n\n"
            f"نوع الصفحة: {type_desc}\n"
            f"نبرة الكتابة: {tone_desc}\n"
            f"{lang_instruction}\n\n"
            f"## 1. قسم البطل (Hero Section)\n"
            f"- **العنوان الرئيسي** (Headline): جملة قوية تجذب الانتباه فورًا (أقل من 10 كلمات)\n"
            f"- **العنوان الفرعي** (Sub-headline): توضيح للعنوان الرئيسي (جملة أو جملتين)\n"
            f"- **نص الدعم**: فقرة قصيرة تشرح القيمة الأساسية\n"
            f"- **زر CTA الرئيسي**: نص الزر + لون مقترح\n"
            f"- **عنصر الثقة**: (عدد العملاء / تقييم / شعارات شركاء)\n\n"
            f"## 2. قسم المشكلة (Pain Points)\n"
            f"- 4-6 نقاط ألم يعاني منها الجمهور المستهدف\n"
            f"- صياغة عاطفية تجعل القارئ يقول \"هذا أنا بالضبط!\"\n"
            f"- تضخيم المشكلة (Agitation) قبل تقديم الحل\n\n"
            f"## 3. قسم الحل (Solution)\n"
            f"- تقديم المنتج/الخدمة كالحل المثالي\n"
            f"- كيف يعمل (3 خطوات بسيطة)\n"
            f"- الانتقال من الألم إلى الراحة\n\n"
            f"## 4. قسم المزايا والفوائد (Features & Benefits)\n"
            f"- 6-8 مزايا مع تحويل كل ميزة إلى فائدة\n"
            f"- لكل ميزة: العنوان + الوصف + الأيقونة المقترحة\n\n"
            f"## 5. قسم الدليل الاجتماعي (Social Proof)\n"
            f"- 3 شهادات عملاء (نموذج واقعي: الاسم، الوظيفة، الشهادة، النتيجة)\n"
            f"- إحصائيات مقنعة (عدد العملاء، نسبة الرضا، النتائج)\n"
            f"- شعارات شركات/وسائل إعلام (اقتراحات)\n\n"
            f"## 6. قسم العرض والسعر (Offer & Pricing)\n"
            f"- تقديم العرض بشكل جذاب\n"
            f"- المكونات والبونصات\n"
            f"- السعر مع تأطير القيمة (Value Framing)\n"
            f"- الضمان وإزالة المخاطر\n\n"
            f"## 7. قسم الأسئلة الشائعة (FAQ)\n"
            f"- 6-8 أسئلة شائعة مع إجابات تزيل الاعتراضات\n"
            f"- كل إجابة تنتهي بتعزيز الرغبة في الشراء\n\n"
            f"## 8. قسم CTA النهائي\n"
            f"- عنوان تحفيزي أخير\n"
            f"- ملخص سريع للقيمة\n"
            f"- زر CTA مع نص قوي\n"
            f"- عنصر إلحاح (ندرة / عداد / موعد نهائي)\n\n"
            f"## 9. عناصر SEO\n"
            f"- عنوان الصفحة (Meta Title) - أقل من 60 حرف\n"
            f"- وصف الصفحة (Meta Description) - أقل من 155 حرف\n"
            f"- 5 كلمات مفتاحية مقترحة\n\n"
            f"## 10. ملاحظات تصميمية\n"
            f"- اقتراحات للألوان والتخطيط\n"
            f"- أماكن الصور/الفيديو المقترحة\n"
            f"- نصائح لتحسين معدل التحويل"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_ab_variants(self, headline: str, count: int = 5, language: str = "ar") -> str:
        system = (
            "أنت خبير في اختبارات A/B وكتابة العناوين الرئيسية (Headlines) عالية التحويل. "
            "تفهم ما يجعل العنوان يجذب الانتباه ويحفز النقر والتحويل في السوق العربي."
        )
        lang_instruction = "اكتب العناوين باللغة العربية." if language == "ar" else "Write headlines in English."
        prompt = (
            f"العنوان الأصلي:\n{headline}\n\n"
            f"{lang_instruction}\n\n"
            f"اكتب {count} نسخ بديلة لاختبار A/B، لكل نسخة:\n\n"
            f"1. **العنوان البديل**: النص الكامل\n"
            f"2. **الأسلوب**: (فضول / خوف من الفوات / سؤال / رقم / قصة / مقارنة / أمر مباشر)\n"
            f"3. **الإطار النفسي**: (PAS / AIDA / Before-After / Social Proof)\n"
            f"4. **الطول**: عدد الكلمات\n"
            f"5. **نقطة القوة**: لماذا قد يتفوق على الأصلي\n"
            f"6. **العنوان الفرعي المقترح**: مكمّل للعنوان\n\n"
            f"## توصيات الاختبار:\n"
            f"- ترتيب الأولوية للاختبار\n"
            f"- حجم العينة المطلوب لنتائج ذات دلالة\n"
            f"- مدة الاختبار المقترحة\n"
            f"- المقياس الأساسي (CTR vs Conversion Rate)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, product: str, page_type: str = "sales", tone: str = "professional", language: str = "ar") -> str:
        content = self.generate(product, page_type, tone, language)
        filename = timestamp_filename("landing_page_copy", "md")
        return save_output(content, filename, str(get_output_dir("landing_page_copy")))


def main():
    parser = argparse.ArgumentParser(description="AI Landing Page Copy Generator - مولد نصوص صفحات الهبوط بالذكاء الاصطناعي")
    parser.add_argument("--product", "-p", required=True, help="وصف المنتج أو الخدمة")
    parser.add_argument("--type", "-t", dest="page_type", default="sales",
                        choices=["sales", "squeeze", "webinar", "coming_soon", "product"],
                        help="نوع صفحة الهبوط")
    parser.add_argument("--tone", default="professional",
                        choices=["professional", "casual", "urgent", "luxury"],
                        help="نبرة الكتابة")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"], help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ في ملف")
    args = parser.parse_args()

    gen = LandingPageCopyGenerator()
    if args.save:
        path = gen.generate_and_save(args.product, args.page_type, args.tone, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.product, args.page_type, args.tone, args.language))


if __name__ == "__main__":
    main()
