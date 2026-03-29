"""AI Customer Journey Mapper - Income Stream #57.
Business Model: رسم خرائط رحلة العميل بالذكاء الاصطناعي (1,500-6,000 ريال/خريطة)
Usage: python -m income_streams.customer_journey.journey_mapper --business "متجر إلكتروني للأزياء" --persona "نساء 25-35" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class CustomerJourneyMapper:
    def __init__(self):
        self.client = AIClient(module_name="customer_journey")

    def generate(self, business: str, persona: str = "", language: str = "ar") -> str:
        system = (
            "أنت استراتيجي تجربة عملاء (CX Strategist) معتمد في تصميم تجربة العملاء "
            "بخبرة تزيد عن 10 سنوات في رسم أكثر من 300 خريطة رحلة عميل لعلامات تجارية سعودية وخليجية. "
            "عملت مع شركات التجارة الإلكترونية والبنوك وشركات الاتصالات والمستشفيات والجهات الحكومية في المنطقة. "
            "تفهم السلوك الشرائي للمستهلك العربي والعوامل الثقافية المؤثرة في تجربته. "
            "تتقن منهجيات Service Blueprint وExperience Mapping وJobs-to-be-Done. "
            "تصمم خرائط رحلة عميل شاملة تحدد نقاط الألم وفرص التحسين وتقيس الأثر على رضا العميل والإيرادات. "
            "تركز على القنوات الرقمية الأكثر استخداماً في المنطقة: واتساب، إنستغرام، سناب شات، تويتر، وتيك توك."
        )
        lang_instruction = (
            "قدم الخريطة باللغة العربية مع المصطلحات التخصصية الإنجليزية عند الحاجة."
            if language == "ar"
            else "Present the journey map in English with MENA cultural context."
        )
        persona_section = f"\nالشخصية المستهدفة (Persona): {persona}" if persona else ""
        prompt = (
            f"ارسم خريطة رحلة عميل (Customer Journey Map) شاملة ومفصلة:\n\n"
            f"النشاط التجاري: {business}\n"
            f"{persona_section}\n"
            f"{lang_instruction}\n\n"
            f"## 0. ملف الشخصية (Persona Profile)\n"
            f"- الاسم والعمر والمهنة\n"
            f"- الأهداف والتحديات\n"
            f"- القنوات المفضلة\n"
            f"- سلوك الشراء والميزانية\n"
            f"- الاقتباس التمثيلي (Representative Quote)\n\n"
            f"---\n\n"
            f"لكل مرحلة من المراحل الخمس التالية، قدم تحليلاً مفصلاً يشمل جميع العناصر:\n\n"
            f"## المرحلة 1: الوعي (Awareness)\n"
            f"- **نقاط التماس (Touchpoints):** جميع القنوات والوسائط التي يتعرف من خلالها العميل على العلامة (إعلانات سوشال ميديا، محركات البحث، توصيات الأصدقاء، المؤثرين، إلخ)\n"
            f"- **مشاعر العميل (Customer Emotions):** الحالة النفسية والعاطفية في هذه المرحلة (فضول، حيرة، اهتمام مبدئي)\n"
            f"- **نقاط الألم (Pain Points):** المشاكل والإحباطات التي يواجهها العميل\n"
            f"- **الفرص (Opportunities):** فرص التحسين والتميز عن المنافسين\n"
            f"- **الإجراءات المطلوبة (Actions Needed):** ما يجب على الشركة فعله في هذه المرحلة\n"
            f"- **مؤشرات الأداء (KPIs):** مقاييس النجاح (معدل الوصول، الانطباعات، CTR، تكلفة الاكتساب)\n"
            f"- **تكتيكات القنوات (Channel Tactics):** إجراءات محددة لكل قناة (واتساب، إنستغرام، سناب، تويتر، قوقل)\n\n"
            f"## المرحلة 2: التفكير والبحث (Consideration)\n"
            f"- **نقاط التماس:** زيارة الموقع، مقارنة المنتجات، قراءة التقييمات، التواصل مع خدمة العملاء\n"
            f"- **مشاعر العميل:** التردد، المقارنة، البحث عن التأكيد\n"
            f"- **نقاط الألم:** صعوبة المقارنة، نقص المعلومات، عدم الثقة\n"
            f"- **الفرص:** محتوى مقنع، شهادات عملاء، تجربة مجانية\n"
            f"- **الإجراءات المطلوبة:** تحسين صفحات المنتج، إعادة الاستهداف، محتوى تعليمي\n"
            f"- **مؤشرات الأداء:** معدل الارتداد، وقت البقاء، صفحات لكل جلسة، معدل إضافة للسلة\n"
            f"- **تكتيكات القنوات:** لكل قناة تفصيلاً\n\n"
            f"## المرحلة 3: القرار والشراء (Decision)\n"
            f"- **نقاط التماس:** صفحة الدفع، العروض، كود الخصم، خدمة العملاء الفورية\n"
            f"- **مشاعر العميل:** الحماس، القلق من القرار، الخوف من الندم\n"
            f"- **نقاط الألم:** تعقيد الدفع، خيارات الشحن المحدودة، عدم وضوح سياسة الإرجاع\n"
            f"- **الفرص:** تبسيط الدفع، ضمانات، عروض اللحظة الأخيرة\n"
            f"- **الإجراءات المطلوبة:** تحسين صفحة الدفع، تنويع وسائل الدفع (مدى، Apple Pay، تمارا)\n"
            f"- **مؤشرات الأداء:** معدل التحويل، معدل التخلي عن السلة، متوسط قيمة الطلب\n"
            f"- **تكتيكات القنوات:** لكل قناة تفصيلاً\n\n"
            f"## المرحلة 4: الاحتفاظ (Retention)\n"
            f"- **نقاط التماس:** تأكيد الطلب، التتبع، التوصيل، الاستخدام الأول، الدعم الفني\n"
            f"- **مشاعر العميل:** الترقب، الرضا أو خيبة الأمل، التقييم\n"
            f"- **نقاط الألم:** تأخر التوصيل، اختلاف المنتج عن الصورة، صعوبة التواصل\n"
            f"- **الفرص:** تجربة فتح مميزة (Unboxing)، متابعة استباقية، برنامج ولاء\n"
            f"- **الإجراءات المطلوبة:** رسائل متابعة، استبيان رضا، عروض إعادة الشراء\n"
            f"- **مؤشرات الأداء:** NPS، معدل إعادة الشراء، CLV، معدل الاحتفاظ\n"
            f"- **تكتيكات القنوات:** لكل قناة تفصيلاً\n\n"
            f"## المرحلة 5: التأييد والترويج (Advocacy)\n"
            f"- **نقاط التماس:** طلب التقييم، برنامج الإحالة، المجتمع، السوشال ميديا\n"
            f"- **مشاعر العميل:** الفخر، الانتماء، الرغبة في المشاركة\n"
            f"- **نقاط الألم:** عدم وجود حافز للمشاركة، صعوبة كتابة التقييم\n"
            f"- **الفرص:** برنامج سفراء، محتوى من العملاء (UGC)، مكافآت الإحالة\n"
            f"- **الإجراءات المطلوبة:** تفعيل برنامج إحالة، طلب تقييمات، بناء مجتمع\n"
            f"- **مؤشرات الأداء:** معدل الإحالة، عدد التقييمات، معدل المشاركة، Viral Coefficient\n"
            f"- **تكتيكات القنوات:** لكل قناة تفصيلاً\n\n"
            f"---\n\n"
            f"## ملخص تنفيذي\n"
            f"- أهم 5 نقاط ألم يجب معالجتها فوراً\n"
            f"- أهم 5 فرص للتحسين السريع (Quick Wins)\n"
            f"- خارطة طريق التنفيذ (30/60/90 يوم)\n"
            f"- الميزانية التقديرية للتحسينات\n"
            f"- العائد المتوقع على الاستثمار في تحسين التجربة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_touchpoint_audit(self, business: str, channels: str = "", language: str = "ar") -> str:
        system = (
            "أنت مدقق نقاط تماس العملاء (Touchpoint Auditor) متخصص في تقييم وتحسين "
            "جميع نقاط التفاعل بين العلامة التجارية والعميل في السوق العربي. "
            "تقيّم كل نقطة تماس من حيث الفعالية والاتساق والتأثير على تجربة العميل الكلية. "
            "تقدم توصيات عملية مبنية على بيانات وأفضل الممارسات العالمية المكيّفة للسوق المحلي."
        )
        lang_instruction = (
            "قدم التدقيق باللغة العربية مع مصطلحات تخصصية إنجليزية."
            if language == "ar"
            else "Present the audit in English with MENA context."
        )
        channels_section = f"\nالقنوات الحالية: {channels}" if channels else ""
        prompt = (
            f"أجرِ تدقيقاً شاملاً لنقاط تماس العملاء (Touchpoint Audit):\n\n"
            f"النشاط التجاري: {business}\n"
            f"{channels_section}\n"
            f"{lang_instruction}\n\n"
            f"## 1. خريطة نقاط التماس الكاملة\n"
            f"- قائمة بجميع نقاط التماس مرتبة حسب مرحلة الرحلة\n"
            f"- تصنيف كل نقطة (رقمية/فيزيائية/بشرية)\n"
            f"- مستوى الأهمية (حرج/مهم/ثانوي)\n\n"
            f"## 2. تقييم القنوات الرقمية\n"
            f"لكل قناة (الموقع، التطبيق، واتساب، إنستغرام، تويتر، سناب شات، تيك توك):\n"
            f"- التقييم الحالي (1-10)\n"
            f"- نقاط القوة والضعف\n"
            f"- فرص التحسين الفورية\n"
            f"- مقارنة مع أفضل الممارسات\n\n"
            f"## 3. تقييم القنوات التقليدية\n"
            f"- الفروع/المتاجر الفعلية\n"
            f"- الهاتف وخدمة العملاء\n"
            f"- المواد المطبوعة والتغليف\n\n"
            f"## 4. فجوات التجربة (Experience Gaps)\n"
            f"- الفجوات بين القنوات (Omnichannel Gaps)\n"
            f"- نقاط الانقطاع في الرحلة\n"
            f"- التناقضات في الرسائل والتجربة\n\n"
            f"## 5. لحظات الحقيقة (Moments of Truth)\n"
            f"- لحظة الحقيقة الصفرية (ZMOT) - البحث الأولي\n"
            f"- لحظة الحقيقة الأولى (FMOT) - أول تفاعل\n"
            f"- لحظة الحقيقة الثانية (SMOT) - تجربة الاستخدام\n"
            f"- لحظة الحقيقة النهائية (UMOT) - المشاركة والتقييم\n\n"
            f"## 6. خطة التحسين المرتبة حسب الأولوية\n"
            f"- تحسينات فورية (0-30 يوم)\n"
            f"- تحسينات متوسطة المدى (1-3 أشهر)\n"
            f"- تحسينات استراتيجية (3-6 أشهر)\n"
            f"- الأثر المتوقع والتكلفة التقديرية لكل تحسين"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, business: str, persona: str = "", language: str = "ar") -> str:
        content = self.generate(business, persona=persona, language=language)
        filename = timestamp_filename("customer_journey", "md")
        return save_output(content, filename, str(get_output_dir("journeys")))


def main():
    parser = argparse.ArgumentParser(description="AI Customer Journey Mapper - راسم خرائط رحلة العميل بالذكاء الاصطناعي")
    parser.add_argument("--business", "-b", required=True, help="وصف النشاط التجاري")
    parser.add_argument("--persona", "-p", default="", help="وصف الشخصية المستهدفة")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="اللغة الأساسية")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = CustomerJourneyMapper()
    if args.save:
        path = gen.generate_and_save(args.business, persona=args.persona, language=args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.business, persona=args.persona, language=args.language))


if __name__ == "__main__":
    main()
