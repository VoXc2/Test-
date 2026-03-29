"""AI Academic Assistant - Research papers, abstracts, literature reviews.
Usage: python -m income_streams.academic_assistant.assistant --topic "تأثير AI على التعليم" --type research
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class AcademicAssistant:
    """Academic research assistant. NOT for producing ready-to-submit papers."""

    def __init__(self):
        self.client = AIClient()

    def generate_outline(self, topic, paper_type="research", pages=20, language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"باحث أكاديمي ومحرر علمي خبير بـ{lang}. تساعد في هيكلة الأبحاث وتتبع معايير APA. "
            "تنويه: أداة مساعدة وليست لإنتاج بحوث جاهزة للتسليم."
        )
        prompt = f"""أنشئ هيكل بحث أكاديمي:
الموضوع: {topic}
النوع: {paper_type}
الصفحات: {pages}

أعطني:
1. العنوان المقترح
2. الملخص (Abstract) - 250 كلمة
3. الكلمات المفتاحية
4. هيكل البحث التفصيلي (كل فصل مع العناوين الفرعية)
5. منهجية البحث المقترحة
6. 15-20 مرجع مقترح (مواضيع للبحث عنها)
7. النتائج المتوقعة
8. التوصيات المحتملة"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=3500)

    def generate_abstract(self, topic, findings=""):
        system = "كاتب ملخصات أكاديمية. يكتب abstracts واضحة ومقنعة تتبع معايير APA."
        prompt = f"اكتب ملخص أكاديمي (250 كلمة) عن: {topic}\n{'النتائج: ' + findings if findings else ''}"
        return self.client.generate(prompt, system_prompt=system, max_tokens=1000)

    def generate_literature_review(self, topic, sources=""):
        system = "باحث أكاديمي خبير في مراجعة الأدبيات. ينظم المصادر حسب المواضيع ويحدد الفجوات البحثية."
        prompt = f"اكتب مراجعة أدبيات عن: {topic}\n{'المصادر: ' + sources if sources else 'اقترح مصادر مناسبة'}"
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic, **kw):
        content = self.generate_outline(topic, **kw)
        return save_output(content, timestamp_filename(f"academic_{topic}", "md"), str(get_output_dir("reports")))

def main():
    parser = argparse.ArgumentParser(description="Academic Assistant - مساعد أكاديمي")
    parser.add_argument("--topic", "-t", required=True)
    parser.add_argument("--type", default="research", choices=["research", "thesis", "review", "case_study"])
    parser.add_argument("--pages", "-p", type=int, default=20)
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    assistant = AcademicAssistant()
    if args.save:
        print(f"Saved to: {assistant.generate_and_save(args.topic, paper_type=args.type, pages=args.pages, language=args.language)}")
    else:
        print(assistant.generate_outline(args.topic, args.type, args.pages, args.language))

if __name__ == "__main__":
    main()
