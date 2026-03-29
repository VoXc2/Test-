"""Affiliate Program Builder - Income Stream #58.
Business Model: بناء برامج التسويق بالعمولة للعلامات التجارية ($500 - $5,000 لكل برنامج)
Usage: python -m income_streams.affiliate_program.program_builder --product "اسم المنتج" --model percentage --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class AffiliateProgramBuilder:
    """AI-powered affiliate program design and asset generation system."""

    def __init__(self):
        self.client = AIClient(module_name="affiliate_program")

    def generate(self, product: str, commission_model: str = "percentage", language: str = "ar") -> str:
        """Generate a complete affiliate program structure with commission tiers and recruitment strategy.

        Args:
            product: Product or brand name to build the affiliate program for.
            commission_model: Commission structure - percentage, fixed, tiered, or recurring.
            language: Output language (ar for Arabic, en for English).
        """
        system = (
            "أنت مهندس برامج تسويق بالعمولة (Affiliate Marketing Architect) بخبرة تتجاوز 12 عامًا "
            "في بناء برامج أفلييت حققت إيرادات تفوق 5 مليون دولار لعلامات تجارية رائدة في التجارة "
            "الإلكترونية بمنطقة الخليج العربي. متخصص في تصميم هياكل العمولات المتدرجة (tiered commissions)، "
            "واستراتيجيات استقطاب الشركاء (partner recruitment)، وأنظمة التتبع والإسناد (tracking & attribution). "
            "لديك خبرة عميقة في منصات مثل Impact، ShareASale، وPartnerStack، بالإضافة إلى بناء برامج مخصصة. "
            "تفهم سلوك المسوقين بالعمولة في السوق العربي وتعرف كيف تحفزهم لتحقيق أعلى أداء. "
            "أجب بلغة عربية احترافية مع مصطلحات تقنية دقيقة."
        )

        commission_models = {
            "percentage": "نسبة مئوية من كل عملية بيع",
            "fixed": "مبلغ ثابت لكل عملية بيع أو إحالة",
            "tiered": "نسب متدرجة تزداد مع حجم المبيعات",
            "recurring": "عمولة متكررة على الاشتراكات الشهرية/السنوية",
        }
        model_desc = commission_models.get(commission_model, commission_models["percentage"])

        lang_instruction = "اكتب المحتوى بالكامل باللغة العربية." if language == "ar" else "Write the entire content in English."

        prompt = f"""صمم برنامج تسويق بالعمولة متكامل واحترافي للمنتج/العلامة التجارية التالية:

المنتج: {product}
نموذج العمولة المطلوب: {commission_model} ({model_desc})
{lang_instruction}

أريد برنامج أفلييت شامل يتضمن الأقسام التالية بالتفصيل:

## 1. هيكل البرنامج (Program Structure)
- اسم البرنامج وهويته
- الأهداف الرئيسية (KPIs)
- الجمهور المستهدف من الشركاء
- المنصة/الأداة المقترحة للإدارة

## 2. هيكل العمولات - 3 مستويات (Commission Tiers)
### المستوى البرونزي (Bronze)
- نسبة/مبلغ العمولة، شروط التأهل، حد أدنى للسحب
### المستوى الفضي (Silver)
- نسبة/مبلغ العمولة المحسّن، شروط الترقية، مزايا إضافية
### المستوى الذهبي (Gold)
- أعلى نسبة عمولة، امتيازات حصرية، دعم مخصص

## 3. الشروط والأحكام (Terms & Conditions)
- مدة ملف تعريف الارتباط (cookie duration)
- طرق الدفع والجدول الزمني
- السياسات المحظورة (brand bidding, spam, etc.)
- حقوق العلامة التجارية واستخدام الأصول
- شروط الإنهاء والتعليق

## 4. استراتيجية استقطاب الشركاء (Recruitment Strategy)
- القنوات المستهدفة لاستقطاب المسوقين (مؤثرين، مدونين، مقارنات، كوبونات)
- رسالة الدعوة النموذجية
- معايير القبول والرفض
- خطة الوصول للـ 100 شريك الأوائل

## 5. حزمة الأصول الترويجية (Promotional Assets Package)
- 3 قوالب بريد إلكتروني (تعريفي، عرض خاص، متابعة)
- 5 منشورات سوشال ميديا جاهزة (تويتر/X، إنستغرام، لينكدإن)
- نقاط حوار رئيسية (talking points) للمسوقين
- نصوص إعلانية مقترحة

## 6. توصيات التتبع والتقنية (Tracking Recommendations)
- منصة التتبع المقترحة
- إعداد الروابط والكوبونات
- تقارير الأداء المطلوبة
- تكامل مع أدوات التحليل

## 7. تسلسل التهيئة (Onboarding Sequence)
- رسالة ترحيبية
- دليل البدء السريع (خطوات عملية)
- جدول تدريبي أسبوعي
- قائمة الأسئلة الشائعة

## 8. مكافآت الأداء (Performance Bonuses)
- مكافأة أول بيعة
- مكافآت شهرية للأداء المتميز
- برنامج المسوق المميز (Super Affiliate)
- مسابقات وتحديات موسمية

اجعل البرنامج عمليًا وجاهزًا للتنفيذ مع أرقام وتفاصيل محددة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_affiliate_assets(self, product: str, asset_type: str = "email", language: str = "ar") -> str:
        """Generate promotional assets for affiliates.

        Args:
            product: Product or brand name.
            asset_type: Type of asset - email, social, banner, or all.
            language: Output language.
        """
        system = (
            "أنت كاتب محتوى تسويقي متخصص في إنشاء أصول ترويجية عالية التحويل لبرامج التسويق بالعمولة. "
            "تكتب نصوصًا مقنعة تجمع بين الإبداع والبيع المباشر، مع فهم عميق لسيكولوجية الشراء "
            "في السوق العربي. خبير في كتابة رسائل البريد الإلكتروني، منشورات السوشال ميديا، "
            "ونصوص البانرات الإعلانية التي تحقق معدلات نقر (CTR) تتجاوز المعدل العام."
        )

        asset_types = {
            "email": "قوالب بريد إلكتروني (email swipes) - 5 رسائل مختلفة: تعريفية، عرض خاص، قصة نجاح، مقارنة، آخر فرصة",
            "social": "منشورات سوشال ميديا - 10 منشورات لـ: تويتر/X (3)، إنستغرام (3)، فيسبوك (2)، لينكدإن (2)",
            "banner": "نصوص بانرات إعلانية - 8 نصوص بأحجام مختلفة: leaderboard, skyscraper, square, rectangle",
            "all": "جميع الأصول الترويجية: بريد إلكتروني، سوشال ميديا، بانرات، ونقاط حوار",
        }
        asset_desc = asset_types.get(asset_type, asset_types["email"])

        lang_instruction = "اكتب جميع الأصول باللغة العربية." if language == "ar" else "Write all assets in English."

        prompt = f"""أنشئ أصولًا ترويجية احترافية للمسوقين بالعمولة للمنتج التالي:

المنتج: {product}
نوع الأصول المطلوبة: {asset_desc}
{lang_instruction}

لكل أصل ترويجي، قدم:
- العنوان/الموضوع
- النص الكامل جاهز للاستخدام
- دعوة لاتخاذ إجراء (CTA) واضحة
- ملاحظات للمسوق حول أفضل وقت ومكان للاستخدام
- [AFFILIATE_LINK] كعنصر نائب لرابط المسوق

اجعل النصوص مقنعة وعملية وجاهزة للنسخ واللصق مباشرة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, product: str, commission_model: str = "percentage", language: str = "ar") -> str:
        """Generate a complete affiliate program and save to file.

        Returns:
            Path to the saved file.
        """
        content = self.generate(product, commission_model, language)
        filename = timestamp_filename("affiliate_program", "md")
        return save_output(content, filename, str(get_output_dir("affiliate_program")))


def main():
    parser = argparse.ArgumentParser(description="Affiliate Program Builder - بناء برامج التسويق بالعمولة")
    parser.add_argument("--product", "-p", required=True, help="Product or brand name")
    parser.add_argument("--model", "-m", choices=["percentage", "fixed", "tiered", "recurring"],
                        default="percentage", help="Commission model type (default: percentage)")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"],
                        help="Output language (default: ar)")
    parser.add_argument("--assets", "-a", choices=["email", "social", "banner", "all"],
                        help="Generate promotional assets instead of full program")
    parser.add_argument("--save", "-s", action="store_true", help="Save output to file")

    args = parser.parse_args()
    gen = AffiliateProgramBuilder()

    if args.assets:
        content = gen.generate_affiliate_assets(args.product, args.assets, args.language)
        print(content)
    elif args.save:
        path = gen.generate_and_save(args.product, args.model, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.product, args.model, args.language))


if __name__ == "__main__":
    main()
