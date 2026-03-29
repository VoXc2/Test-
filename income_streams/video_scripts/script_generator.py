"""AI Video Script Generator - Income Stream #18.
Business Model: كتابة سيناريوهات فيديو بالذكاء الاصطناعي (50-300 ريال/سيناريو)
Usage: python -m income_streams.video_scripts.script_generator --topic "الموضوع" --type youtube --duration "10min" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class VideoScriptGenerator:
    def __init__(self):
        self.client = AIClient(module_name="video_scripts")

    def generate(self, topic: str, video_type: str = "youtube", duration: str = "10min", language: str = "ar") -> str:
        system = (
            "أنت كاتب سيناريو فيديو محترف بخبرة تزيد عن 10 سنوات في إنتاج المحتوى الرقمي على يوتيوب وريلز وتيك توك والإعلانات. "
            "تكتب سيناريوهات تجذب المشاهد من أول 3 ثواني وتحافظ على انتباهه حتى النهاية باستخدام تقنيات السرد القصصي وعلم النفس. "
            "تفهم خوارزميات كل منصة وتحسّن السيناريو لزيادة وقت المشاهدة والتفاعل والمشاركة. "
            "تكتب بأسلوب حواري طبيعي يناسب الجمهور العربي مع مراعاة الثقافة المحلية. "
            "تعرف أحدث الاتجاهات في صناعة المحتوى الرقمي العربي."
        )
        lang_instruction = "اكتب السيناريو باللغة العربية." if language == "ar" else "Write the script in English."
        type_map = {
            "youtube": "فيديو يوتيوب طويل",
            "reels": "ريلز/شورت (أقل من 60 ثانية)",
            "ad": "إعلان تجاري",
            "tutorial": "فيديو تعليمي/شرح",
            "explainer": "فيديو توضيحي (Explainer Video)"
        }
        type_desc = type_map.get(video_type, type_map["youtube"])
        prompt = (
            f"اكتب سيناريو {type_desc} عن: {topic}\n"
            f"المدة المستهدفة: {duration}\n"
            f"{lang_instruction}\n\n"
            f"السيناريو يجب أن يتضمن:\n\n"
            f"## Hook (أول 3 ثواني)\n"
            f"- جملة افتتاحية صادمة أو سؤال مثير تجذب المشاهد فورًا\n\n"
            f"## المقدمة (15-30 ثانية)\n"
            f"- تقديم الموضوع وما سيستفيده المشاهد\n\n"
            f"## المحتوى الرئيسي (مع Timestamps)\n"
            f"- تقسيم المحتوى لأجزاء واضحة مع وقت كل جزء\n"
            f"- لكل جزء: النص الحواري الكامل + تعليمات الأداء\n\n"
            f"## CTA (دعوة للتفاعل)\n"
            f"- اشتراك، لايك، تعليق، مشاركة\n\n"
            f"## ملاحظات الإنتاج:\n"
            f"- **ملاحظات التصوير**: زوايا الكاميرا، الإضاءة، الخلفية\n"
            f"- **B-roll مقترح**: لقطات إضافية لكل مشهد\n"
            f"- **الموسيقى/المؤثرات الصوتية**: نوع الموسيقى والمؤثرات لكل جزء\n"
            f"- **وصف Thumbnail**: تصميم الصورة المصغرة (النص، الألوان، تعبير الوجه)\n"
            f"- **العنوان المقترح**: 3 خيارات محسّنة لـ SEO\n"
            f"- **الوصف**: وصف الفيديو محسّن للبحث\n"
            f"- **الهاشتاقات**: 10-15 هاشتاق مناسب"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_short(self, topic: str, platform: str = "reels") -> str:
        system = (
            "أنت خبير في كتابة سيناريوهات الفيديوهات القصيرة (ريلز، تيك توك، شورتس). "
            "تكتب محتوى فيروسي مصمم للانتشار السريع مع hook قوي في أول ثانية. "
            "تفهم خوارزميات المنصات القصيرة وكيفية تحقيق أعلى معدل مشاهدة."
        )
        prompt = (
            f"اكتب سيناريو فيديو قصير لـ {platform} عن: {topic}\n\n"
            f"المدة: 15-60 ثانية\n"
            f"المطلوب:\n"
            f"1. Hook (أول ثانية): جملة صادمة/سؤال/حقيقة غريبة\n"
            f"2. المحتوى: مباشر ومكثف بدون مقدمات\n"
            f"3. النهاية: مفاجأة أو CTA أو cliffhanger\n"
            f"4. النص على الشاشة (Captions)\n"
            f"5. الموسيقى/الصوت المقترح (ترند أو أصلي)\n"
            f"6. تعليمات التصوير والمونتاج\n"
            f"7. الهاشتاقات (10 هاشتاقات)\n"
            f"8. أفضل وقت للنشر"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_ad_script(self, product: str, target_audience: str) -> str:
        system = (
            "أنت كاتب إعلانات فيديو محترف متخصص في الإعلانات الرقمية على سناب شات وإنستغرام ويوتيوب. "
            "تكتب إعلانات تحقق أعلى معدلات تحويل باستخدام صيغ مثبتة مثل AIDA وPAS. "
            "تفهم سلوك المستهلك السعودي والخليجي."
        )
        prompt = (
            f"اكتب سيناريو إعلان فيديو للمنتج/الخدمة: {product}\n"
            f"الجمهور المستهدف: {target_audience}\n\n"
            f"أنشئ 3 نسخ مختلفة:\n"
            f"1. **إعلان 15 ثانية** (سناب شات/ستوري)\n"
            f"2. **إعلان 30 ثانية** (إنستغرام/فيسبوك)\n"
            f"3. **إعلان 60 ثانية** (يوتيوب)\n\n"
            f"لكل نسخة:\n"
            f"- السيناريو كاملاً (نص + تعليمات بصرية)\n"
            f"- Hook يوقف التصفح\n"
            f"- عرض المشكلة والحل\n"
            f"- الدليل الاجتماعي\n"
            f"- CTA واضح ومحفز\n"
            f"- ملاحظات الإنتاج"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        content = self.generate(topic, **kwargs)
        return save_output(content, timestamp_filename("video_script", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Video Script Generator - مولد سيناريوهات الفيديو بالذكاء الاصطناعي")
    parser.add_argument("--topic", "-t", required=True, help="موضوع الفيديو")
    parser.add_argument("--type", choices=["youtube", "reels", "ad", "tutorial", "explainer"], default="youtube", help="نوع الفيديو")
    parser.add_argument("--duration", "-d", default="10min", help="مدة الفيديو (افتراضي: 10min)")
    parser.add_argument("--language", "-l", choices=["ar", "en"], default="ar", help="لغة السيناريو")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = VideoScriptGenerator()
    if args.save:
        path = gen.generate_and_save(args.topic, video_type=args.type, duration=args.duration, language=args.language)
        print(f"Saved to: {path}")
    else:
        print(gen.generate(args.topic, video_type=args.type, duration=args.duration, language=args.language))


if __name__ == "__main__":
    main()
