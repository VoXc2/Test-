"""Launch Sequence Planner - Income Stream #59.
Business Model: تخطيط وإدارة إطلاق المنتجات الرقمية ($1,000 - $10,000 لكل حملة إطلاق)
Usage: python -m income_streams.launch_sequence.launch_planner --product "اسم المنتج" --type plf --days 14 --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class LaunchSequencePlanner:
    """AI-powered product launch sequence planning and email generation system."""

    def __init__(self):
        self.client = AIClient(module_name="launch_sequence")

    def generate(self, product: str, launch_type: str = "plf", days: int = 14, language: str = "ar") -> str:
        """Generate a complete product launch plan with email sequences and content strategy.

        Args:
            product: Product or service to launch.
            launch_type: Launch methodology - seed, plf, webinar, challenge, or flash_sale.
            days: Total launch duration in days.
            language: Output language (ar for Arabic, en for English).
        """
        system = (
            "أنت استراتيجي إطلاق منتجات (Product Launch Strategist) مدرّب على منهجية Jeff Walker's "
            "Product Launch Formula (PLF)، وأطر عمل Ryan Deiss لتسلسلات الإطلاق، وقمع الويبينار "
            "الخاص بـ Sam Ovens. لديك خبرة تتجاوز 10 سنوات في إطلاق المنتجات الرقمية في سوق الشرق "
            "الأوسط وشمال أفريقيا (MENA)، وأطلقت أكثر من 50 منتجًا رقميًا بإيرادات إجمالية تفوق "
            "3 مليون دولار. تفهم نفسية المشتري العربي، وأوقات الذروة في التفاعل، والعوامل الثقافية "
            "المؤثرة في قرار الشراء (الثقة، الشهادات، الضمانات). متخصص في بناء تسلسلات إطلاق تخلق "
            "ترقبًا حقيقيًا وتحقق مبيعات قوية من اليوم الأول. أجب بلغة عربية احترافية مع خطط عملية قابلة للتنفيذ."
        )

        launch_types = {
            "seed": "إطلاق بذري (Seed Launch) - اختبار المنتج مع جمهور صغير وجمع شهادات",
            "plf": "إطلاق PLF (Product Launch Formula) - تسلسل 3-4 فيديوهات تعليمية + فتح السلة",
            "webinar": "إطلاق عبر ويبينار (Webinar Launch) - ندوة مباشرة + عرض في النهاية",
            "challenge": "إطلاق عبر تحدي (Challenge Launch) - تحدي 5-7 أيام ثم عرض المنتج",
            "flash_sale": "تخفيض سريع (Flash Sale) - عرض محدود المدة بخصم كبير",
        }
        type_desc = launch_types.get(launch_type, launch_types["plf"])

        lang_instruction = "اكتب الخطة بالكامل باللغة العربية." if language == "ar" else "Write the entire plan in English."

        prompt = f"""صمم خطة إطلاق منتج متكاملة واحترافية:

المنتج: {product}
نوع الإطلاق: {launch_type} ({type_desc})
مدة الإطلاق: {days} يوم
{lang_instruction}

أريد خطة إطلاق شاملة تتضمن الأقسام التالية:

## 1. خطة المحتوى قبل الإطلاق (Pre-Launch Content Plan)
- جدول زمني يومي من اليوم -{days} إلى يوم الإطلاق
- أنواع المحتوى لكل يوم (فيديو، بوست، ستوري، بث مباشر)
- الرسالة الرئيسية لكل مرحلة
- منصات النشر المقترحة

## 2. استراتيجية الإطلاق البذري (Seed Launch Strategy)
- كيفية اختبار العرض مع جمهور محدود (50-100 شخص)
- جمع الشهادات والتوصيات (social proof)
- تحسين العرض بناءً على التغذية الراجعة
- تحويل المشاركين الأوائل لسفراء

## 3. تسلسلات البريد الإلكتروني لكل مرحلة
### مرحلة البذر (Seed Phase) - 3 رسائل
- رسالة الاستطلاع والاهتمام
- رسالة القيمة المجانية
- رسالة الدعوة الحصرية

### مرحلة ما قبل الإطلاق (Pre-Launch) - 5 رسائل
- رسالة التشويق والترقب
- رسالة القصة والمشكلة
- رسالة الحل والتحول
- رسالة الإثبات الاجتماعي
- رسالة الإعلان عن موعد الفتح

### مرحلة فتح السلة (Cart Open) - 4 رسائل
- رسالة الإعلان الرسمي
- رسالة التفاصيل والمزايا
- رسالة الأسئلة الشائعة
- رسالة المكافأة الإضافية

### مرحلة إغلاق السلة (Cart Close) - 4 رسائل
- رسالة التذكير (48 ساعة)
- رسالة الندرة (24 ساعة)
- رسالة الفرصة الأخيرة (6 ساعات)
- رسالة الإغلاق النهائي (ساعة واحدة)

## 4. منشورات السوشال ميديا
- 3 منشورات تشويقية
- 3 منشورات تعليمية (قيمة مجانية)
- 3 منشورات إثبات اجتماعي
- 3 منشورات بيعية مباشرة

## 5. استراتيجية العد التنازلي (Countdown Strategy)
- تصميم صفحة العد التنازلي
- رسائل العد التنازلي عبر القنوات
- أساليب خلق الإلحاح (urgency)

## 6. سكريبت يوم الإطلاق (Launch Day Script)
- جدول اليوم ساعة بساعة
- رسائل كل قناة
- خطة الطوارئ (إذا كانت المبيعات أقل من المتوقع)

## 7. تكتيكات الندرة والإلحاح (Scarcity & Urgency)
- 5 تكتيكات أخلاقية وفعالة
- كيفية تطبيق كل تكتيك
- أمثلة على الصياغة

## 8. متابعة ما بعد الإطلاق (Post-Launch Follow-up)
- رسائل شكر للمشترين
- تسلسل التهيئة للعملاء الجدد
- خطة لغير المشترين (downsell / waitlist)
- تحليل وتقييم الأداء

## 9. المقاييس المطلوب تتبعها (Metrics to Track)
- مقاييس ما قبل الإطلاق (حجم القائمة، معدل الفتح، التفاعل)
- مقاييس يوم الإطلاق (المبيعات، معدل التحويل، الإيرادات)
- مقاييس ما بعد الإطلاق (الاسترجاعات، رضا العملاء، LTV)

اجعل الخطة عملية مع تواريخ وأوقات محددة وأمثلة حقيقية على الرسائل."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_launch_emails(self, product: str, phase: str = "pre_launch", language: str = "ar") -> str:
        """Generate phase-specific launch emails.

        Args:
            product: Product or service name.
            phase: Launch phase - seed, pre_launch, cart_open, or cart_close.
            language: Output language.
        """
        system = (
            "أنت كاتب بريد إلكتروني تسويقي متخصص في تسلسلات إطلاق المنتجات. تكتب رسائل "
            "تحقق معدلات فتح تتجاوز 40% ومعدلات نقر تتجاوز 8% في السوق العربي. تجمع بين "
            "السرد القصصي المشوّق والبيع النفسي الذكي مع احترام ثقافة وقيم الجمهور العربي. "
            "كل رسالة تكتبها لها هدف واحد واضح ودعوة لاتخاذ إجراء لا يمكن تجاهلها."
        )

        phases = {
            "seed": "مرحلة البذر - اختبار الفكرة وجمع أوائل المهتمين (3 رسائل)",
            "pre_launch": "مرحلة ما قبل الإطلاق - بناء الترقب والرغبة (5 رسائل)",
            "cart_open": "مرحلة فتح السلة - تحويل المهتمين لمشترين (4 رسائل)",
            "cart_close": "مرحلة إغلاق السلة - الإلحاح والندرة (4 رسائل)",
        }
        phase_desc = phases.get(phase, phases["pre_launch"])

        lang_instruction = "اكتب جميع الرسائل باللغة العربية." if language == "ar" else "Write all emails in English."

        prompt = f"""اكتب تسلسل رسائل بريد إلكتروني كامل لمرحلة الإطلاق التالية:

المنتج: {product}
المرحلة: {phase} ({phase_desc})
{lang_instruction}

لكل رسالة قدم:
1. **سطر الموضوع** (Subject Line) - 3 خيارات لكل رسالة
2. **نص المعاينة** (Preview Text)
3. **نص الرسالة الكامل** مع تنسيق HTML بسيط
4. **دعوة لاتخاذ إجراء** (CTA) رئيسية
5. **توقيت الإرسال** المقترح (اليوم والساعة)
6. **ملاحظات تقنية** (شريحة الجمهور المستهدفة، A/B test suggestions)

اجعل الرسائل مقنعة وعاطفية وعملية، جاهزة للنسخ إلى أي منصة بريد إلكتروني."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, product: str, launch_type: str = "plf", days: int = 14, language: str = "ar") -> str:
        """Generate a complete launch plan and save to file.

        Returns:
            Path to the saved file.
        """
        content = self.generate(product, launch_type, days, language)
        filename = timestamp_filename("launch_plan", "md")
        return save_output(content, filename, str(get_output_dir("launch_sequence")))


def main():
    parser = argparse.ArgumentParser(description="Launch Sequence Planner - مخطط تسلسل الإطلاق")
    parser.add_argument("--product", "-p", required=True, help="Product or service to launch")
    parser.add_argument("--type", "-t", choices=["seed", "plf", "webinar", "challenge", "flash_sale"],
                        default="plf", help="Launch methodology (default: plf)")
    parser.add_argument("--days", "-d", type=int, default=14,
                        help="Total launch duration in days (default: 14)")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"],
                        help="Output language (default: ar)")
    parser.add_argument("--emails", "-e", choices=["seed", "pre_launch", "cart_open", "cart_close"],
                        help="Generate phase-specific emails instead of full plan")
    parser.add_argument("--save", "-s", action="store_true", help="Save output to file")

    args = parser.parse_args()
    gen = LaunchSequencePlanner()

    if args.emails:
        content = gen.generate_launch_emails(args.product, args.emails, args.language)
        print(content)
    elif args.save:
        path = gen.generate_and_save(args.product, args.type, args.days, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.product, args.type, args.days, args.language))


if __name__ == "__main__":
    main()
