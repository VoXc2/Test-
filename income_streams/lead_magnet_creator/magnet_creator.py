"""AI Lead Magnet Creator - Income Stream #55.
Business Model: إنشاء مغناطيسات العملاء المحتملين بالذكاء الاصطناعي (300-2,000 ريال/مغناطيس)
Usage: python -m income_streams.lead_magnet_creator.magnet_creator --niche "التسويق الرقمي" --type checklist --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class LeadMagnetCreator:
    def __init__(self):
        self.client = AIClient(module_name="lead_magnet_creator")

    def generate(self, niche: str, magnet_type: str = "checklist", audience: str = "", language: str = "ar") -> str:
        system = (
            "أنت استراتيجي تسويق رقمي متخصص في توليد العملاء المحتملين (Lead Generation) "
            "بخبرة تزيد عن 12 سنة في بناء أكثر من 200 مغناطيس عملاء ناجح لسوق الشرق الأوسط وشمال أفريقيا. "
            "عملت مع شركات SaaS وتجارة إلكترونية ومقدمي خدمات في السعودية والإمارات ومصر. "
            "تفهم سيكولوجية اتخاذ القرار عند الجمهور العربي وما يدفعهم لتحميل المحتوى المجاني. "
            "تصمم مغناطيسات عملاء تحقق معدلات تحويل تتجاوز 40% من خلال تقديم قيمة فورية وملموسة. "
            "تتقن صياغة العناوين الجذابة والوعود المقنعة التي تحل مشكلة حقيقية للجمهور المستهدف."
        )
        lang_instruction = (
            "قدم المحتوى باللغة العربية الفصحى مع مصطلحات تسويقية إنجليزية عند الحاجة."
            if language == "ar"
            else "Present all content in English with Arabic market context where relevant."
        )
        audience_section = f"\nالجمهور المستهدف: {audience}" if audience else ""
        type_map = {
            "checklist": "قائمة مراجعة (Checklist) - 15-20 عنصر قابل للتنفيذ مع مربعات اختيار",
            "ebook": "كتاب إلكتروني مصغر (Mini Ebook) - 10-15 صفحة مع فصول وعناوين فرعية",
            "template": "قالب جاهز (Template) - نموذج قابل للتعبئة مع تعليمات وأمثلة",
            "quiz": "اختبار تفاعلي (Quiz) - 10-15 سؤال مع نظام تسجيل وتصنيف النتائج",
            "mini_course": "دورة مصغرة (Mini Course) - 5 دروس قصيرة بالبريد الإلكتروني",
            "swipe_file": "ملف نماذج جاهزة (Swipe File) - مجموعة قوالب ونصوص قابلة للنسخ والتعديل",
        }
        type_desc = type_map.get(magnet_type, type_map["checklist"])
        prompt = (
            f"أنشئ مغناطيس عملاء محتملين (Lead Magnet) متكامل وعالي التحويل:\n\n"
            f"المجال/النيتش: {niche}\n"
            f"نوع المغناطيس: {type_desc}\n"
            f"{audience_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم المحتوى التالي بالتفصيل:\n\n"
            f"## 1. العنوان الرئيسي (3 خيارات)\n"
            f"لكل خيار: العنوان + العنوان الفرعي + سبب فعاليته + معدل التحويل المتوقع\n\n"
            f"## 2. العنوان الفرعي والوعد\n"
            f"- الوعد الرئيسي (ما سيحصل عليه القارئ)\n"
            f"- الإطار الزمني للنتائج\n"
            f"- عبارة القيمة الفريدة (UVP)\n\n"
            f"## 3. جدول المحتويات / الهيكل\n"
            f"- تقسيم تفصيلي للأقسام مع وصف مختصر لكل قسم\n"
            f"- الترتيب المنطقي للمحتوى\n\n"
            f"## 4. المحتوى الكامل\n"
            f"{'- 15-20 عنصر مع شرح مفصل لكل عنصر وخطوات التنفيذ وأمثلة واقعية' if magnet_type == 'checklist' else ''}"
            f"{'- مخطط الفصول (5-7 فصول) مع النقاط الرئيسية والأمثلة والاقتباسات والإحصائيات لكل فصل' if magnet_type == 'ebook' else ''}"
            f"{'- القالب الكامل مع حقول قابلة للتعبئة وتعليمات واضحة ومثال معبأ كنموذج' if magnet_type == 'template' else ''}"
            f"{'- 10-15 سؤال مع خيارات متعددة ونظام تسجيل النقاط وتفسير النتائج (3-4 فئات)' if magnet_type == 'quiz' else ''}"
            f"{'- 5 دروس بريدية: لكل درس عنوان وملخص ومحتوى تفصيلي وتمرين عملي وCTA' if magnet_type == 'mini_course' else ''}"
            f"{'- مجموعة من 10-15 قالب/نموذج جاهز مع تعليمات التخصيص وأمثلة الاستخدام' if magnet_type == 'swipe_file' else ''}\n\n"
            f"## 5. نسخة صفحة التحميل (Download Page)\n"
            f"- العنوان الرئيسي والفرعي\n"
            f"- 5-7 نقاط فوائد (Bullet Points) بأسلوب مقنع\n"
            f"- عبارة الحث على الإجراء (CTA)\n"
            f"- عنصر الاستعجال (Urgency)\n"
            f"- شهادة اجتماعية مقترحة (Social Proof)\n\n"
            f"## 6. سلسلة البريد الإلكتروني المتابعة (5 رسائل)\n"
            f"لكل رسالة: عنوان الرسالة + سطر الموضوع + المحتوى + CTA + توقيت الإرسال\n"
            f"- رسالة 1: التسليم والترحيب (فوري)\n"
            f"- رسالة 2: تعزيز القيمة (يوم 1)\n"
            f"- رسالة 3: قصة نجاح (يوم 3)\n"
            f"- رسالة 4: محتوى إضافي (يوم 5)\n"
            f"- رسالة 5: العرض المدفوع (يوم 7)\n\n"
            f"## 7. استراتيجية التوزيع\n"
            f"- أفضل القنوات للترويج\n"
            f"- نصوص إعلانية مقترحة لكل قناة\n"
            f"- ميزانية مقترحة وعائد الاستثمار المتوقع"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_opt_in_page(self, magnet_title: str, benefits: str = "", language: str = "ar") -> str:
        system = (
            "أنت كاتب إعلانات متخصص في صفحات الاشتراك (Opt-in Pages) وتحسين معدلات التحويل. "
            "صممت أكثر من 500 صفحة اشتراك لعلامات تجارية عربية بمعدل تحويل يتراوح بين 35%-65%. "
            "تتقن أساليب الإقناع مثل AIDA وPAS وتفهم الدوافع النفسية للجمهور العربي."
        )
        lang_instruction = (
            "اكتب النسخة باللغة العربية مع عبارات تسويقية مؤثرة."
            if language == "ar"
            else "Write the copy in English optimized for MENA audience."
        )
        benefits_section = f"\nالفوائد الرئيسية: {benefits}" if benefits else ""
        prompt = (
            f"اكتب نسخة صفحة اشتراك (Opt-in Page) عالية التحويل:\n\n"
            f"عنوان المغناطيس: {magnet_title}\n"
            f"{benefits_section}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. قسم البطل (Hero Section)\n"
            f"- العنوان الرئيسي (H1) - 3 نسخ للاختبار A/B\n"
            f"- العنوان الفرعي (H2)\n"
            f"- وصف مختصر (2-3 سطور)\n"
            f"- زر CTA (3 نسخ)\n\n"
            f"## 2. قسم المشكلة\n"
            f"- 3-5 نقاط ألم يعاني منها الجمهور\n"
            f"- سؤال محفز للتفكير\n\n"
            f"## 3. قسم الحل والفوائد\n"
            f"- 7 نقاط فوائد مع أيقونات مقترحة\n"
            f"- ما الذي سيتعلمه القارئ\n\n"
            f"## 4. معاينة المحتوى\n"
            f"- وصف ما بداخل المغناطيس\n"
            f"- صورة الغلاف المقترحة (وصف)\n\n"
            f"## 5. الإثبات الاجتماعي\n"
            f"- 3 شهادات مقترحة\n"
            f"- أرقام وإحصائيات\n\n"
            f"## 6. نموذج الاشتراك\n"
            f"- الحقول المطلوبة\n"
            f"- نص الخصوصية\n"
            f"- نص الزر\n\n"
            f"## 7. قسم الأسئلة الشائعة (3-5 أسئلة)\n\n"
            f"## 8. ملاحظات التصميم والتحسين\n"
            f"- توصيات الألوان والتخطيط\n"
            f"- عناصر الاستعجال والندرة\n"
            f"- نصائح تحسين معدل التحويل"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, niche: str, magnet_type: str = "checklist", audience: str = "", language: str = "ar") -> str:
        content = self.generate(niche, magnet_type=magnet_type, audience=audience, language=language)
        filename = timestamp_filename("lead_magnet", "md")
        return save_output(content, filename, str(get_output_dir("lead_magnets")))


def main():
    parser = argparse.ArgumentParser(description="AI Lead Magnet Creator - مولد مغناطيسات العملاء بالذكاء الاصطناعي")
    parser.add_argument("--niche", "-n", required=True, help="المجال أو النيتش المستهدف")
    parser.add_argument("--type", "-t", dest="magnet_type", choices=["checklist", "ebook", "template", "quiz", "mini_course", "swipe_file"], default="checklist", help="نوع المغناطيس")
    parser.add_argument("--audience", "-a", default="", help="وصف الجمهور المستهدف")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = LeadMagnetCreator()
    if args.save:
        path = gen.generate_and_save(args.niche, magnet_type=args.magnet_type, audience=args.audience, language=args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.niche, magnet_type=args.magnet_type, audience=args.audience, language=args.language))


if __name__ == "__main__":
    main()
