"""AI Hashtag Strategist - Income Stream #43.
Business Model: استراتيجية هاشتاقات السوشال ميديا بالذكاء الاصطناعي
Usage: python -m income_streams.hashtag_strategist.strategist --niche "عقارات" --platform instagram --content-type post --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class HashtagStrategist:
    def __init__(self):
        self.client = AIClient(module_name="hashtag_strategist")

    def generate(self, niche: str, platform: str = "instagram", content_type: str = "post", language: str = "ar") -> str:
        system = (
            "خبير سوشال ميديا متخصص في استراتيجيات الهاشتاقات وخوارزميات المنصات. "
            "يعرف الهاشتاقات العربية والخليجية الأكثر فعالية. "
            "يفهم خوارزمية كل منصة وكيف تؤثر الهاشتاقات على الوصول والتفاعل. "
            "يتابع الترندات العربية والعالمية بشكل يومي ويعرف الهاشتاقات المحظورة والمقيدة."
        )
        lang_instruction = "قدم المحتوى باللغة العربية." if language == "ar" else "Present content in English."
        platform_map = {
            "instagram": "إنستغرام (حد 30 هاشتاق، الأمثل 20-25)",
            "twitter": "تويتر/إكس (حد 3-5 هاشتاقات فعالة)",
            "tiktok": "تيكتوك (حد 5-8 هاشتاقات، التركيز على الترندات)",
            "linkedin": "لينكدإن (حد 3-5 هاشتاقات مهنية)"
        }
        platform_desc = platform_map.get(platform, platform_map["instagram"])
        prompt = (
            f"أنشئ استراتيجية هاشتاقات شاملة للمجال التالي:\n"
            f"المجال: {niche}\n"
            f"المنصة: {platform_desc}\n"
            f"نوع المحتوى: {content_type}\n"
            f"{lang_instruction}\n\n"
            f"قدم التالي:\n\n"
            f"## 1. هاشتاقات عالية المنافسة (10 هاشتاقات)\n"
            f"لكل هاشتاق: الهاشتاق + عدد المنشورات التقريبي + نسبة الوصول المتوقعة\n\n"
            f"## 2. هاشتاقات متوسطة المنافسة (10 هاشتاقات)\n"
            f"لكل هاشتاق: الهاشتاق + عدد المنشورات التقريبي + لماذا هو فعال\n\n"
            f"## 3. هاشتاقات منخفضة المنافسة (10 هاشتاقات)\n"
            f"لكل هاشتاق: الهاشتاق + فرصة التصدر + الجمهور المستهدف\n\n"
            f"## 4. استراتيجية الاستخدام\n"
            f"- التوزيع الأمثل (كم من كل فئة)\n"
            f"- مكان وضع الهاشتاقات (في المنشور أم في التعليق)\n"
            f"- التدوير وعدم التكرار\n"
            f"- أفضل الأوقات للنشر مع كل مجموعة\n\n"
            f"## 5. هاشتاقات ممنوعة/محظورة\n"
            f"- قائمة الهاشتاقات المحظورة في هذا المجال\n"
            f"- هاشتاقات Shadow Ban الشائعة\n"
            f"- كيف تتجنب الحظر\n\n"
            f"## 6. هاشتاقات موسمية\n"
            f"- هاشتاقات المناسبات القادمة\n"
            f"- هاشتاقات رمضان/العيد/اليوم الوطني\n"
            f"- هاشتاقات الموسم الحالي\n\n"
            f"## 7. نصائح احترافية\n"
            f"- أخطاء شائعة في استخدام الهاشتاقات\n"
            f"- أدوات تتبع أداء الهاشتاقات\n"
            f"- كيف تنشئ هاشتاق خاص بعلامتك التجارية\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def analyze_trending(self, niche: str, platform: str = "instagram") -> str:
        system = (
            "خبير سوشال ميديا متخصص في تحليل الترندات والهاشتاقات الرائجة. "
            "يتابع الترندات العربية والخليجية بشكل مستمر ويفهم أسباب انتشارها."
        )
        prompt = (
            f"حلل الهاشتاقات الرائجة حالياً في مجال '{niche}' على منصة {platform}:\n\n"
            f"## 1. الهاشتاقات الرائجة الآن\n"
            f"- أعلى 10 هاشتاقات رائجة مع تحليل سبب الرواج\n\n"
            f"## 2. توقعات الترند القادم\n"
            f"- هاشتاقات متوقع أن ترتفع خلال الأسبوع القادم\n\n"
            f"## 3. فرص الركوب على الترند\n"
            f"- كيف تستفيد من الترندات الحالية في مجالك\n"
            f"- أمثلة على محتوى يربط بين الترند ومجالك\n\n"
            f"## 4. تحليل المنافسين\n"
            f"- هاشتاقات يستخدمها المنافسون بنجاح\n"
            f"- فجوات يمكنك استغلالها\n"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_and_save(self, niche: str, **kw) -> str:
        content = self.generate(niche, **kw)
        return save_output(content, timestamp_filename("hashtag_strategy", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Hashtag Strategist - استراتيجية هاشتاقات بالذكاء الاصطناعي")
    parser.add_argument("--niche", required=True, help="المجال أو النيتش")
    parser.add_argument("--platform", default="instagram", choices=["instagram", "twitter", "tiktok", "linkedin"], help="المنصة")
    parser.add_argument("--content-type", default="post", choices=["post", "reel", "story"], help="نوع المحتوى")
    parser.add_argument("--language", default="ar", help="اللغة (ar/en)")
    parser.add_argument("--save", action="store_true", help="حفظ النتيجة في ملف")
    args = parser.parse_args()

    gen = HashtagStrategist()
    if args.save:
        path = gen.generate_and_save(args.niche, platform=args.platform, content_type=args.content_type, language=args.language)
        print(f"تم الحفظ في: {path}")
    else:
        print(gen.generate(args.niche, platform=args.platform, content_type=args.content_type, language=args.language))


if __name__ == "__main__":
    main()
