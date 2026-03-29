"""AI YouTube Optimizer - Titles, descriptions, tags, thumbnails.
Usage: python -m income_streams.youtube_optimizer.optimizer --topic "شرح ChatGPT" --niche "تقنية"
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class YouTubeOptimizer:
    def __init__(self):
        self.client = AIClient()

    def optimize(self, video_topic, niche, target_audience="", language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"خبير يوتيوب ومتخصص في YouTube SEO وخوارزمية التوصيات بـ{lang}. "
            "تعرف كيف تحسّن CTR ووقت المشاهدة والترتيب في البحث."
        )
        prompt = f"""حسّن فيديو يوتيوب:
الموضوع: {video_topic}
النيتش: {niche}
{"الجمهور: " + target_audience if target_audience else ""}

أعطني:
1. 10 عناوين (مرتبة بالقوة) - كل عنوان أقل من 60 حرف
2. الوصف المحسّن (مع timestamps وروابط)
3. Tags (30+ كلمة مفتاحية)
4. وصف Thumbnail (3 خيارات)
5. Chapters المقترحة
6. End Screen CTA
7. Cards المقترحة
8. كلمات مفتاحية للبحث"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_title_variations(self, topic, count=10):
        system = "خبير عناوين يوتيوب. اكتب عناوين جذابة تزيد CTR."
        return self.client.generate(f"اكتب {count} عناوين يوتيوب لفيديو عن: {topic}", system_prompt=system, max_tokens=1000)

    def generate_and_save(self, topic, **kw):
        content = self.optimize(topic, **kw)
        return save_output(content, timestamp_filename(f"youtube_{topic}", "md"), str(get_output_dir("reports")))

def main():
    parser = argparse.ArgumentParser(description="YouTube Optimizer - محسّن يوتيوب")
    parser.add_argument("--topic", "-t", required=True)
    parser.add_argument("--niche", "-n", required=True)
    parser.add_argument("--audience", "-a", default="")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    opt = YouTubeOptimizer()
    if args.save:
        path = opt.generate_and_save(args.topic, niche=args.niche, target_audience=args.audience, language=args.language)
        print(f"Saved to: {path}")
    else:
        print(opt.optimize(args.topic, args.niche, args.audience, args.language))

if __name__ == "__main__":
    main()
