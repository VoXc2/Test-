"""AI Academic Assistant - Income Stream #48.
Business Model: مساعد أكاديمي بالذكاء الاصطناعي
Usage: python -m income_streams.academic_assistant.assistant --topic "أثر الذكاء الاصطناعي على التعليم" --type research --pages 20 --save
**تنويه**: أداة مساعدة وليست لإنتاج بحوث جاهزة للتسليم
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class AcademicAssistant:
    def __init__(self):
        self.client = AIClient(module_name="academic_assistant")

    def generate_outline(self, topic: str, paper_type: str = "research", pages: int = 20, language: str = "ar") -> str:
        system = (
            "باحث أكاديمي ومحرر علمي خبير. "
            "يساعد في هيكلة الأبحاث وكتابة الملخصات ومراجعة المراجع. "
            "يتبع معايير APA/IEEE. "
            "يفهم متطلبات الجامعات السعودية والعربية. "
            "يساعد في تطوير الأفكار البحثية وصياغتها بشكل أكاديمي سليم. "
            "تنويه: هذه أداة مساعدة لتوجيه الباحث وليست لإنتاج بحوث جاهزة للتسليم."
        )
        lang_instruction = "قدم المحتوى باللغة العربية مع المصطلحات الإنجليزية الأكاديمية." if language == "ar" else "Present content in English."
        type_map = {
            "research": "بحث علمي (Research Paper)",
            "thesis": "رسالة ماجستير/دكتوراه (Thesis/Dissertation)",
            "review": "مراجعة أدبيات (Literature Review)",
            "case_study": "دراسة حالة (Case Study)"
        }
        type_desc = type_map.get(paper_type, type_map["research"])
        prompt = (
            f"ساعدني في هيكلة بحث أكاديمي:\n"
            f"الموضوع: {topic}\n"
            f"نوع البحث: {type_desc}\n"
            f"عدد الصفحات المتوقع: {pages}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. هيكل البحث المقترح\n"
            f"- الأبواب والفصول مع عدد الصفحات لكل قسم\n"
            f"- العناوين الرئيسية والفرعية\n"
            f"- تسلسل منطقي للأفكار\n\n"
            f"## 2. الملخص (Abstract)\n"
            f"- ملخص مقترح (150-300 كلمة)\n"
            f"- الكلمات المفتاحية (5-7)\n\n"
            f"## 3. المقدمة المقترحة\n"
            f"- خلفية الموضوع\n"
            f"- المشكلة البحثية\n"
            f"- أسئلة البحث\n"
            f"- أهداف البحث\n"
            f"- أهمية البحث\n"
            f"- حدود البحث\n\n"
            f"## 4. مراجعة الأدبيات\n"
            f"- المحاور الرئيسية للمراجعة\n"
            f"- الدراسات السابقة المقترحة للمراجعة\n"
            f"- الفجوة البحثية\n\n"
            f"## 5. المنهجية المقترحة\n"
            f"- نوع المنهج (كمي/كيفي/مختلط)\n"
            f"- أدوات جمع البيانات\n"
            f"- العينة المقترحة\n"
            f"- أساليب التحليل\n\n"
            f"## 6. النتائج المتوقعة\n"
            f"- النتائج المحتملة\n"
            f"- كيفية عرض النتائج\n\n"
            f"## 7. المراجع المقترحة\n"
            f"- 15-20 مرجع مقترح (كتب + أبحاث + مواقع موثوقة)\n"
            f"- تنسيق APA\n\n"
            f"**تنويه**: هذا مخطط إرشادي لمساعدة الباحث في تنظيم أفكاره وليس بحثاً جاهزاً.\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_abstract(self, topic: str, findings: str = "") -> str:
        system = (
            "باحث أكاديمي خبير في كتابة الملخصات البحثية. "
            "يكتب ملخصات واضحة ومركزة تتبع المعايير الأكاديمية."
        )
        findings_section = f"\nالنتائج الرئيسية: {findings}" if findings else ""
        prompt = (
            f"اكتب ملخص بحث أكاديمي (Abstract) للموضوع التالي:\n"
            f"الموضوع: {topic}\n"
            f"{findings_section}\n\n"
            f"قدم:\n"
            f"- ملخص عربي (200-300 كلمة)\n"
            f"- ملخص إنجليزي (200-300 كلمة)\n"
            f"- الكلمات المفتاحية بالعربي والإنجليزي\n\n"
            f"يجب أن يتضمن الملخص: الهدف، المنهجية، أهم النتائج، التوصيات.\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_literature_review(self, topic: str, sources: str = "") -> str:
        system = (
            "باحث أكاديمي متخصص في مراجعة الأدبيات والدراسات السابقة. "
            "يعرف كيف ينظم المراجع موضوعياً وزمنياً ومنهجياً."
        )
        sources_section = f"\nمراجع متوفرة: {sources}" if sources else ""
        prompt = (
            f"ساعدني في إعداد مراجعة أدبيات للموضوع التالي:\n"
            f"الموضوع: {topic}\n"
            f"{sources_section}\n\n"
            f"قدم:\n"
            f"- المحاور الرئيسية للمراجعة\n"
            f"- تلخيص الدراسات السابقة ذات الصلة\n"
            f"- المقارنة بين الدراسات\n"
            f"- الفجوة البحثية\n"
            f"- الإطار النظري المقترح\n"
            f"- مراجع مقترحة للاطلاع (بتنسيق APA)\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def review_paper(self, paper_text: str) -> str:
        system = (
            "محكّم أكاديمي خبير يراجع الأبحاث بموضوعية ويقدم ملاحظات بنّاءة. "
            "يتبع معايير التحكيم العلمي المعتمدة."
        )
        prompt = (
            f"راجع النص الأكاديمي التالي وقدم ملاحظات تحسينية:\n\n"
            f"{paper_text[:3000]}\n\n"
            f"قدم:\n"
            f"- تقييم عام (1-10)\n"
            f"- نقاط القوة\n"
            f"- نقاط الضعف\n"
            f"- أخطاء لغوية وإملائية\n"
            f"- أخطاء منهجية\n"
            f"- اقتراحات التحسين (مرتبة بالأولوية)\n"
            f"- ملاحظات على التوثيق والمراجع\n"
            f"- التقييم النهائي والتوصية\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic: str, **kw) -> str:
        content = self.generate_outline(topic, **kw)
        return save_output(content, timestamp_filename("academic_outline", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Academic Assistant - مساعد أكاديمي بالذكاء الاصطناعي (أداة مساعدة وليست لإنتاج بحوث جاهزة)")
    parser.add_argument("--topic", required=True, help="موضوع البحث")
    parser.add_argument("--type", default="research", choices=["research", "thesis", "review", "case_study"], dest="paper_type", help="نوع البحث")
    parser.add_argument("--pages", type=int, default=20, help="عدد الصفحات المتوقع")
    parser.add_argument("--language", default="ar", help="اللغة (ar/en)")
    parser.add_argument("--save", action="store_true", help="حفظ النتيجة في ملف")
    args = parser.parse_args()

    gen = AcademicAssistant()
    if args.save:
        path = gen.generate_and_save(args.topic, paper_type=args.paper_type, pages=args.pages, language=args.language)
        print(f"تم الحفظ في: {path}")
    else:
        print(gen.generate_outline(args.topic, paper_type=args.paper_type, pages=args.pages, language=args.language))


if __name__ == "__main__":
    main()
