"""AI Ad Copy Generator - Income Stream #54.
Business Model: كتابة نصوص إعلانية بالذكاء الاصطناعي (200-1,500 ريال/حملة)
Usage: python -m income_streams.ad_copy_generator.ad_generator --product "وصف المنتج" --platform meta --objective conversions --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class AdCopyGenerator:
    def __init__(self):
        self.client = AIClient(module_name="ad_copy_generator")

    def generate(self, product: str, platform: str = "meta", objective: str = "conversions", language: str = "ar") -> str:
        system = (
            "أنت خبير تسويق أداء (Performance Marketing) بخبرة في إدارة ميزانيات إعلانية تتجاوز 10 مليون دولار في منطقة الخليج العربي (GCC). "
            "تتقن كتابة نصوص إعلانية لجميع المنصات: Meta (Facebook/Instagram)، Google (Search/Display)، Snapchat، TikTok. "
            "تفهم خوارزميات كل منصة وتكتب نصوص تحقق أعلى Quality Score وRelevance Score. "
            "حققت نتائج استثنائية مع عملائك: تكلفة اكتساب عميل (CPA) أقل بـ 50% من المتوسط الصناعي. "
            "تكتب إعلانات تجذب الانتباه في أول ثانيتين وتحفز الفعل الفوري. "
            "تراعي المواصفات الفنية لكل منصة (عدد الأحرف، أبعاد الصور، طول الفيديو) وتلتزم بسياسات الإعلانات."
        )
        lang_instruction = "اكتب جميع النصوص الإعلانية باللغة العربية الفصحى المبسطة مع قوة التأثير." if language == "ar" else "Write all ad copy in English optimized for GCC/MENA audience."
        platform_map = {
            "meta": "Meta (Facebook & Instagram): نص أساسي، عناوين متعددة، أوصاف، تنسيقات (صورة/فيديو/كاروسيل)",
            "google_search": "Google Search Ads: عناوين (30 حرف)، أوصاف (90 حرف)، إضافات (Extensions)",
            "google_display": "Google Display Ads: عناوين قصيرة وطويلة، أوصاف، صور بأحجام متعددة",
            "snapchat": "Snapchat Ads: نص قصير ومباشر، عنوان جذاب، CTA واضح، تنسيق عمودي",
            "tiktok": "TikTok Ads: نص إبداعي وعفوي، هوك قوي في أول ثانية، ترند وتحدي"
        }
        platform_desc = platform_map.get(platform, platform_map["meta"])
        objective_map = {
            "awareness": "الوعي بالعلامة التجارية: الوصول لأكبر عدد من الجمهور المستهدف",
            "traffic": "زيارات الموقع: جذب زيارات عالية الجودة للموقع أو التطبيق",
            "conversions": "التحويلات: تحقيق مبيعات أو تسجيلات أو إجراءات محددة",
            "leads": "جمع بيانات العملاء المحتملين: نماذج تسجيل وعروض مجانية"
        }
        objective_desc = objective_map.get(objective, objective_map["conversions"])
        prompt = (
            f"اكتب نصوص إعلانية كاملة للمنتج/الخدمة التالية:\n{product}\n\n"
            f"المنصة: {platform_desc}\n"
            f"الهدف الإعلاني: {objective_desc}\n"
            f"{lang_instruction}\n\n"
            f"## 1. النص الأساسي (Primary Text)\n"
            f"- **النسخة A** (قصيرة - سطرين): نص مباشر ومقنع\n"
            f"- **النسخة B** (متوسطة - 3-4 أسطر): نص مع قصة قصيرة أو مشكلة وحل\n"
            f"- **النسخة C** (طويلة - 5-7 أسطر): نص تفصيلي مع دليل اجتماعي وعرض\n\n"
            f"## 2. العناوين (Headlines)\n"
            f"- 5 عناوين رئيسية (كل عنوان بأسلوب مختلف):\n"
            f"  - عنوان بالأرقام/الإحصائيات\n"
            f"  - عنوان بالسؤال\n"
            f"  - عنوان بالفائدة المباشرة\n"
            f"  - عنوان بالفضول\n"
            f"  - عنوان بالإلحاح/الندرة\n\n"
            f"## 3. الأوصاف (Descriptions)\n"
            f"- 3 أوصاف مختلفة تكمل العنوان\n"
            f"- كل وصف يحتوي على فائدة + CTA\n\n"
            f"## 4. نص زر CTA\n"
            f"- 3 خيارات لنص الزر مناسبة للمنصة والهدف\n"
            f"- تبرير اختيار كل نص\n\n"
            f"## 5. اقتراحات الاستهداف (Audience Targeting)\n"
            f"- **الجمهور الأساسي**: الديموغرافيا، الاهتمامات، السلوكيات\n"
            f"- **جمهور مشابه** (Lookalike): مصدر الجمهور المقترح\n"
            f"- **إعادة الاستهداف** (Retargeting): الشرائح المقترحة\n"
            f"- **الاستثناءات**: من يجب استبعاده\n\n"
            f"## 6. المواصفات الفنية للمنصة\n"
            f"- أبعاد الصور/الفيديو المطلوبة\n"
            f"- الحد الأقصى للأحرف في كل حقل\n"
            f"- أفضل تنسيق (صورة/فيديو/كاروسيل/قصة)\n"
            f"- مدة الفيديو المثالية إن وجد\n\n"
            f"## 7. اقتراحات الصور/الفيديو\n"
            f"- وصف تفصيلي لـ 3 تصاميم مقترحة\n"
            f"- النص على الصورة (Text Overlay) - أقل من 20%\n"
            f"- نصائح للتصوير/التصميم\n\n"
            f"## 8. نصائح لتحسين الأداء\n"
            f"- الميزانية اليومية المقترحة\n"
            f"- استراتيجية المزايدة (Bidding Strategy)\n"
            f"- جدول الإعلانات (Ad Schedule)\n"
            f"- اختبارات A/B المقترحة\n"
            f"- مؤشرات الأداء المستهدفة (CTR, CPC, CPA, ROAS)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_campaign_set(self, product: str, platforms: str = "meta,google,snapchat", language: str = "ar") -> str:
        system = (
            "أنت خبير تسويق متعدد القنوات (Omnichannel Marketing) في منطقة الخليج. "
            "تصمم حملات إعلانية متكاملة عبر منصات متعددة مع رسالة موحدة ومحتوى مخصص لكل منصة. "
            "تفهم نقاط قوة كل منصة وتوزع الميزانية بذكاء لتحقيق أفضل عائد على الإنفاق الإعلاني (ROAS)."
        )
        lang_instruction = "اكتب باللغة العربية." if language == "ar" else "Write in English."
        platform_list = [p.strip() for p in platforms.split(",")]
        prompt = (
            f"صمم حملة إعلانية متكاملة متعددة المنصات للمنتج/الخدمة:\n{product}\n\n"
            f"المنصات المطلوبة: {', '.join(platform_list)}\n"
            f"{lang_instruction}\n\n"
            f"## 1. الاستراتيجية العامة\n"
            f"- الرسالة الموحدة للحملة\n"
            f"- توزيع الميزانية بين المنصات (نسب مئوية مع التبرير)\n"
            f"- مراحل الحملة (وعي → اهتمام → تحويل)\n\n"
        )
        for p in platform_list:
            prompt += (
                f"## منصة {p.upper()}\n"
                f"- 3 نسخ إعلانية (قصيرة/متوسطة/طويلة)\n"
                f"- 3 عناوين\n"
                f"- وصف الصورة/الفيديو المقترح\n"
                f"- الاستهداف المخصص للمنصة\n"
                f"- الميزانية والمزايدة\n"
                f"- KPIs المستهدفة\n\n"
            )
        prompt += (
            f"## التنسيق بين المنصات\n"
            f"- استراتيجية إعادة الاستهداف عبر المنصات (Cross-Platform Retargeting)\n"
            f"- تتبع الأداء الموحد (Attribution)\n"
            f"- جدول النشر والتكرار لكل منصة\n"
            f"- الميزانية الإجمالية والعائد المتوقع"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, product: str, platform: str = "meta", objective: str = "conversions", language: str = "ar") -> str:
        content = self.generate(product, platform, objective, language)
        filename = timestamp_filename("ad_copy", "md")
        return save_output(content, filename, str(get_output_dir("ad_copy_generator")))


def main():
    parser = argparse.ArgumentParser(description="AI Ad Copy Generator - مولد النصوص الإعلانية بالذكاء الاصطناعي")
    parser.add_argument("--product", "-p", required=True, help="وصف المنتج أو الخدمة")
    parser.add_argument("--platform", default="meta",
                        choices=["google_search", "google_display", "meta", "snapchat", "tiktok"],
                        help="المنصة الإعلانية")
    parser.add_argument("--objective", "-o", default="conversions",
                        choices=["awareness", "traffic", "conversions", "leads"],
                        help="الهدف الإعلاني")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"], help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ في ملف")
    args = parser.parse_args()

    gen = AdCopyGenerator()
    if args.save:
        path = gen.generate_and_save(args.product, args.platform, args.objective, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.product, args.platform, args.objective, args.language))


if __name__ == "__main__":
    main()
