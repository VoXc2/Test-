"""AI Feedback Analyzer - Customer sentiment and pattern analysis.
Usage: python -m income_streams.feedback_analyzer.analyzer --feedback "الخدمة ممتازة لكن التوصيل بطيء"
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class FeedbackAnalyzer:
    def __init__(self):
        self.client = AIClient()

    def analyze(self, feedback_text, business="", language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"محلل تجربة عملاء وخبير في Voice of Customer (VoC) بـ{lang}. "
            "تحلل التعليقات وتستخرج أنماط ورؤى عملية. تصنف المشاعر وتحدد الأولويات."
        )
        prompt = f"""حلل تعليقات العملاء التالية:
{"الشركة: " + business if business else ""}

التعليقات:
{feedback_text}

أعطني:
1. تحليل المشاعر (إيجابي/سلبي/محايد مع نسبة)
2. المواضيع الرئيسية المتكررة
3. المشاكل الأكثر ذكراً
4. نقاط القوة المذكورة
5. توصيات التحسين (مرتبة بالأولوية)
6. مؤشر رضا العملاء (تقدير 1-10)
7. خطة عمل مقترحة"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def analyze_batch(self, feedbacks, business=""):
        return self.analyze(feedbacks, business)

    def generate_action_plan(self, analysis):
        system = "خبير تحسين تجربة العملاء. حول التحليل لخطة عمل تنفيذية."
        return self.client.generate(f"حول هذا التحليل لخطة عمل:\n{analysis}", system_prompt=system, max_tokens=2000)

    def generate_and_save(self, feedback_text, **kw):
        content = self.analyze(feedback_text, **kw)
        return save_output(content, timestamp_filename("feedback_analysis", "md"), str(get_output_dir("reports")))

def main():
    parser = argparse.ArgumentParser(description="Feedback Analyzer - محلل التعليقات")
    parser.add_argument("--feedback", "-f", required=True)
    parser.add_argument("--business", "-b", default="")
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    analyzer = FeedbackAnalyzer()
    if args.save:
        print(f"Saved to: {analyzer.generate_and_save(args.feedback, business=args.business)}")
    else:
        print(analyzer.analyze(args.feedback, args.business))

if __name__ == "__main__":
    main()
