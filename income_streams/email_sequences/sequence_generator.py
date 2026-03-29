"""AI Email Marketing Sequence Generator - Income Stream #51.
Business Model: إنشاء سلاسل بريد إلكتروني تسويقية بالذكاء الاصطناعي (300-2,000 ريال/سلسلة)
Usage: python -m income_streams.email_sequences.sequence_generator --product "وصف المنتج" --type nurture --emails 7 --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class EmailSequenceGenerator:
    def __init__(self):
        self.client = AIClient(module_name="email_sequences")

    def generate(self, product: str, sequence_type: str = "nurture", num_emails: int = 7, language: str = "ar") -> str:
        system = (
            "أنت خبير تسويق عبر البريد الإلكتروني بخبرة تزيد عن 12 عامًا في السوق العربي وسوق الشرق الأوسط وشمال أفريقيا (MENA). "
            "تدربت على أفضل قمع مبيعات (funnels) في العالم وحللت آلاف الحملات البريدية الناجحة. "
            "تتقن كتابة رسائل بريدية تحقق معدلات فتح أعلى من 35% ومعدلات نقر أعلى من 8% في السوق العربي. "
            "تفهم سيكولوجية القارئ العربي وتوقيتات الإرسال المثالية في المنطقة العربية. "
            "تكتب عناوين مغرية وجسم رسالة مقنع مع دعوات عمل (CTA) لا تُقاوم. "
            "تراعي الفروق الثقافية والدينية في المحتوى وتتجنب أي محتوى غير ملائم."
        )
        lang_instruction = "اكتب جميع الرسائل باللغة العربية الفصحى السهلة مع استخدام المصطلحات التسويقية الإنجليزية عند الحاجة." if language == "ar" else "Write all emails in English with cultural sensitivity for the MENA market."
        type_map = {
            "welcome": "سلسلة ترحيب: رسائل لاستقبال المشتركين الجدد وبناء العلاقة من اليوم الأول",
            "nurture": "سلسلة رعاية: رسائل لتغذية العملاء المحتملين بمحتوى قيّم وبناء الثقة تدريجيًا",
            "sales": "سلسلة بيع: رسائل مركّزة على تحويل العملاء المحتملين إلى مشترين فعليين",
            "cart_abandonment": "سلسلة استعادة السلة المتروكة: رسائل لإقناع العملاء بإكمال عملية الشراء",
            "re_engagement": "سلسلة إعادة التفاعل: رسائل لإحياء العلاقة مع المشتركين غير النشطين"
        }
        type_desc = type_map.get(sequence_type, type_map["nurture"])
        prompt = (
            f"صمم سلسلة بريد إلكتروني تسويقية كاملة للمنتج/الخدمة التالية:\n{product}\n\n"
            f"نوع السلسلة: {type_desc}\n"
            f"عدد الرسائل المطلوب: {num_emails}\n"
            f"{lang_instruction}\n\n"
            f"## المطلوب لكل رسالة من الرسائل الـ {num_emails}:\n\n"
            f"### الرسالة رقم [N]\n"
            f"- **توقيت الإرسال**: (مثال: بعد الاشتراك مباشرة / بعد يوم واحد / بعد 3 أيام)\n"
            f"- **أفضل يوم ووقت للإرسال**: (مثال: الثلاثاء 10 صباحًا بتوقيت الرياض)\n"
            f"- **هدف الرسالة**: (بناء ثقة / تقديم قيمة / تحفيز شراء)\n\n"
            f"#### عنوان الرسالة (Subject Line):\n"
            f"- العنوان الأساسي (النسخة A)\n"
            f"- العنوان البديل للاختبار (النسخة B)\n"
            f"- نص المعاينة (Preview Text)\n\n"
            f"#### جسم الرسالة (Body Copy):\n"
            f"- التحية والافتتاحية (hook مشوّق)\n"
            f"- المحتوى الرئيسي (قصة / معلومة / عرض)\n"
            f"- الفائدة الأساسية للقارئ\n"
            f"- الدليل الاجتماعي (شهادة / إحصائية / نتيجة)\n"
            f"- دعوة العمل الرئيسية (Primary CTA) - نص الزر + الرابط المقترح\n"
            f"- دعوة عمل ثانوية (Secondary CTA) إن وجدت\n"
            f"- التوقيع والخاتمة\n\n"
            f"#### ملاحظات فنية:\n"
            f"- طول الرسالة المقترح (عدد الكلمات)\n"
            f"- هل تحتاج صور؟ (نعم/لا + وصف الصورة)\n"
            f"- Personalization المقترح (اسم، شركة، إلخ)\n\n"
            f"---\n\n"
            f"## في النهاية قدم:\n"
            f"- **خريطة السلسلة الكاملة** (Timeline/Flow)\n"
            f"- **مؤشرات الأداء المستهدفة** (Open Rate, CTR, Conversion Rate)\n"
            f"- **نصائح لتحسين التسليم** (Deliverability Tips)\n"
            f"- **قواعد التقسيم** (Segmentation Rules) للمتابعة بعد السلسلة\n"
            f"- **سيناريوهات التفرع** (إذا فتح/لم يفتح، إذا نقر/لم ينقر)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_subject_lines(self, topic: str, count: int = 10, language: str = "ar") -> str:
        system = (
            "أنت متخصص في كتابة عناوين البريد الإلكتروني (Subject Lines) عالية الأداء. "
            "تفهم سيكولوجية الفضول والإلحاح والتخصيص. "
            "تكتب عناوين تحقق معدلات فتح استثنائية في السوق العربي مع تجنب كلمات السبام."
        )
        lang_instruction = "اكتب العناوين باللغة العربية." if language == "ar" else "Write subject lines in English."
        prompt = (
            f"اكتب {count} عنوان بريد إلكتروني (Subject Line) للموضوع التالي:\n{topic}\n\n"
            f"{lang_instruction}\n\n"
            f"لكل عنوان قدم:\n"
            f"1. **العنوان**: النص الكامل (أقل من 50 حرف)\n"
            f"2. **نص المعاينة** (Preview Text): مكمّل للعنوان (أقل من 90 حرف)\n"
            f"3. **الأسلوب المستخدم**: (فضول / إلحاح / سؤال / رقم / تخصيص / قصة / صدمة)\n"
            f"4. **معدل الفتح المتوقع**: (تقدير بناءً على خبرتك)\n"
            f"5. **مناسب لـ**: (نوع الجمهور المثالي)\n"
            f"6. **نسخة A/B بديلة**: عنوان بديل للاختبار\n\n"
            f"## نصائح عامة:\n"
            f"- أفضل 3 عناوين للاختبار أولاً\n"
            f"- كلمات يجب تجنبها (Spam Trigger Words)\n"
            f"- أفضل الإيموجي للاستخدام في العناوين"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, product: str, sequence_type: str = "nurture", num_emails: int = 7, language: str = "ar") -> str:
        content = self.generate(product, sequence_type, num_emails, language)
        filename = timestamp_filename("email_sequence", "md")
        return save_output(content, filename, str(get_output_dir("email_sequences")))


def main():
    parser = argparse.ArgumentParser(description="AI Email Sequence Generator - مولد سلاسل البريد الإلكتروني بالذكاء الاصطناعي")
    parser.add_argument("--product", "-p", required=True, help="وصف المنتج أو الخدمة")
    parser.add_argument("--type", "-t", dest="sequence_type", default="nurture",
                        choices=["welcome", "nurture", "sales", "cart_abandonment", "re_engagement"],
                        help="نوع السلسلة البريدية")
    parser.add_argument("--emails", "-e", type=int, default=7, help="عدد الرسائل في السلسلة")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"], help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ في ملف")
    args = parser.parse_args()

    gen = EmailSequenceGenerator()
    if args.save:
        path = gen.generate_and_save(args.product, args.sequence_type, args.emails, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.product, args.sequence_type, args.emails, args.language))


if __name__ == "__main__":
    main()
