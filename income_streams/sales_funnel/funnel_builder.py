"""AI Sales Funnel Builder - Income Stream #52.
Business Model: بناء قمع مبيعات رقمي بالذكاء الاصطناعي (1,000-5,000 ريال/قمع)
Usage: python -m income_streams.sales_funnel.funnel_builder --business "وصف النشاط" --type tripwire --audience "الجمهور" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class SalesFunnelBuilder:
    def __init__(self):
        self.client = AIClient(module_name="sales_funnel")

    def generate(self, business: str, funnel_type: str = "tripwire", audience: str = "", language: str = "ar") -> str:
        system = (
            "أنت استراتيجي تسويق رقمي متخصص في بناء قمع المبيعات (Sales Funnels) بخبرة في تصميم أكثر من 500 قمع مبيعات ناجح في السوق العربي ومنطقة الشرق الأوسط وشمال أفريقيا. "
            "تتقن جميع أنواع القمع: Tripwire، Webinar، Challenge، VSL، Product Launch وغيرها. "
            "تفهم رحلة العميل العربي من أول نقطة تواصل إلى الشراء والولاء. "
            "حققت نتائج مبهرة مع عملائك بمعدلات تحويل تتجاوز المعايير الصناعية بـ 3 أضعاف. "
            "تصمم كل مرحلة من القمع بعناية مع محتوى مقنع ورسائل متسلسلة تبني الثقة وتحفز الشراء. "
            "تعتمد على البيانات والتحليلات في تحسين كل مرحلة من مراحل القمع."
        )
        lang_instruction = "قدم الاستراتيجية باللغة العربية مع المصطلحات التسويقية الإنجليزية عند الحاجة." if language == "ar" else "Present the strategy in English with MENA market cultural considerations."
        type_map = {
            "tripwire": "قمع Tripwire: عرض منخفض السعر لتحويل الزائر إلى عميل، ثم ارتقاء بالعروض",
            "webinar": "قمع Webinar: ندوة مجانية تقدم قيمة عالية ثم عرض المنتج الأساسي",
            "challenge": "قمع التحدي (Challenge): تحدي مجاني لعدة أيام يبني الالتزام ثم يقدم العرض",
            "vsl": "قمع فيديو المبيعات (VSL): فيديو مبيعات طويل يقنع المشاهد بالشراء مباشرة",
            "product_launch": "قمع إطلاق المنتج (Product Launch): سلسلة محتوى تبني الترقب قبل الإطلاق"
        }
        type_desc = type_map.get(funnel_type, type_map["tripwire"])
        audience_section = f"\nالجمهور المستهدف: {audience}" if audience else ""
        prompt = (
            f"صمم قمع مبيعات رقمي متكامل للنشاط التالي:\n{business}\n\n"
            f"نوع القمع: {type_desc}\n"
            f"{audience_section}\n"
            f"{lang_instruction}\n\n"
            f"## 1. نظرة عامة على القمع\n"
            f"- ملخص الاستراتيجية\n"
            f"- الأهداف الرئيسية (KPIs)\n"
            f"- الميزانية المقترحة\n"
            f"- العائد المتوقع (ROI)\n\n"
            f"## 2. مرحلة الوعي - TOFU (Top of Funnel)\n"
            f"- مصادر الزيارات (إعلانات، محتوى، شراكات)\n"
            f"- نص الإعلان / المحتوى الجاذب (Lead Magnet)\n"
            f"- صفحة الهبوط (عنوان، وصف، CTA)\n"
            f"- نسبة التحويل المستهدفة\n\n"
            f"## 3. مرحلة الاهتمام - MOFU (Middle of Funnel)\n"
            f"- سلسلة الرسائل البريدية (ملخص كل رسالة)\n"
            f"- المحتوى التعليمي / القيّم\n"
            f"- بناء الثقة والمصداقية\n"
            f"- التفاعل عبر السوشال ميديا\n"
            f"- نسبة التحويل المستهدفة\n\n"
            f"## 4. مرحلة القرار - BOFU (Bottom of Funnel)\n"
            f"- صفحة المبيعات (العنوان، النقاط الرئيسية، العرض)\n"
            f"- نص العرض الرئيسي\n"
            f"- الضمانات وإزالة المخاطر\n"
            f"- الشهادات والدليل الاجتماعي\n"
            f"- CTA الرئيسي ونص الزر\n"
            f"- صفحة الدفع (Checkout Page) - عناصرها\n"
            f"- نسبة التحويل المستهدفة\n\n"
            f"## 5. سلسلة الارتقاء بالمبيعات (Upsell/Downsell)\n"
            f"- عرض الارتقاء الأول (One-Time Offer)\n"
            f"- عرض الارتقاء الثاني\n"
            f"- العرض البديل (Downsell) لمن لم يشتر\n"
            f"- صفحة الشكر (Thank You Page)\n\n"
            f"## 6. سلسلة البريد الإلكتروني بين المراحل\n"
            f"- رسائل ما قبل الشراء (5-7 رسائل مع ملخص كل واحدة)\n"
            f"- رسائل ما بعد الشراء (onboarding)\n"
            f"- رسائل استعادة السلة المتروكة\n"
            f"- رسائل إعادة التفاعل\n\n"
            f"## 7. مقاييس الأداء والتحسين\n"
            f"- مقاييس كل مرحلة (معدل التحويل، التكلفة، القيمة)\n"
            f"- نقاط التسرب المحتملة وحلولها\n"
            f"- اختبارات A/B المقترحة\n"
            f"- خطة التحسين المستمر\n\n"
            f"## 8. الأدوات والتقنيات المطلوبة\n"
            f"- أدوات بناء الصفحات\n"
            f"- أدوات البريد الإلكتروني\n"
            f"- أدوات الدفع\n"
            f"- أدوات التحليل والتتبع"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_upsell_sequence(self, product: str, price_points: str = "", language: str = "ar") -> str:
        system = (
            "أنت خبير في استراتيجيات الارتقاء بالمبيعات (Upsell/Downsell) في السوق العربي. "
            "تصمم عروض لا تُقاوم تزيد متوسط قيمة الطلب (AOV) بنسبة 40-60%. "
            "تفهم نفسية المشتري العربي وتوقيت تقديم العروض الإضافية بدقة."
        )
        lang_instruction = "اكتب باللغة العربية." if language == "ar" else "Write in English."
        price_section = f"\nنقاط السعر المتاحة: {price_points}" if price_points else ""
        prompt = (
            f"صمم استراتيجية ارتقاء بالمبيعات (Upsell/Downsell) للمنتج:\n{product}\n"
            f"{price_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. سلّم القيمة (Value Ladder)\n"
            f"- المنتج الأساسي وسعره\n"
            f"- 3 عروض ارتقاء (Upsells) بأسعار تصاعدية\n"
            f"- 2 عروض بديلة (Downsells) لمن يرفض\n"
            f"- عرض VIP / Premium\n\n"
            f"## 2. نصوص صفحات العروض\n"
            f"- عنوان كل عرض\n"
            f"- النقاط الرئيسية (3-5 نقاط)\n"
            f"- السعر والخصم\n"
            f"- CTA وعداد الوقت\n"
            f"- نص زر القبول ونص زر الرفض\n\n"
            f"## 3. توقيت العروض\n"
            f"- ترتيب ظهور العروض\n"
            f"- المدة الزمنية لكل عرض\n"
            f"- الشروط المنطقية (إذا قبل/رفض)\n\n"
            f"## 4. التوقعات المالية\n"
            f"- متوسط قيمة الطلب المتوقع\n"
            f"- نسبة قبول كل عرض\n"
            f"- الإيرادات الإضافية المتوقعة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, business: str, funnel_type: str = "tripwire", audience: str = "", language: str = "ar") -> str:
        content = self.generate(business, funnel_type, audience, language)
        filename = timestamp_filename("sales_funnel", "md")
        return save_output(content, filename, str(get_output_dir("sales_funnel")))


def main():
    parser = argparse.ArgumentParser(description="AI Sales Funnel Builder - بناء قمع المبيعات بالذكاء الاصطناعي")
    parser.add_argument("--business", "-b", required=True, help="وصف النشاط التجاري")
    parser.add_argument("--type", "-t", dest="funnel_type", default="tripwire",
                        choices=["tripwire", "webinar", "challenge", "vsl", "product_launch"],
                        help="نوع قمع المبيعات")
    parser.add_argument("--audience", "-a", default="", help="وصف الجمهور المستهدف")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"], help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ في ملف")
    args = parser.parse_args()

    gen = SalesFunnelBuilder()
    if args.save:
        path = gen.generate_and_save(args.business, args.funnel_type, args.audience, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.business, args.funnel_type, args.audience, args.language))


if __name__ == "__main__":
    main()
