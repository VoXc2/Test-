"""AI TikTok Script Engine - Viral short-form video scripts.
Usage: python -m income_streams.tiktok_scripts.script_writer --niche "تعليم" --style storytelling
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class TikTokScriptWriter:
    def __init__(self):
        self.client = AIClient()

    def generate(self, niche, style="storytelling", duration=60, language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"صانع محتوى تيكتوك محترف يفهم الخوارزمية بـ{lang}. "
            "تكتب سيناريوهات viral تجذب من أول ثانية. تعرف الترندات."
        )
        prompt = f"""اكتب سيناريو تيكتوك/ريلز:
النيتش: {niche}
الأسلوب: {style}
المدة: {duration} ثانية

أعطني:
1. Hook (أول 1-3 ثواني) - أهم جزء
2. السيناريو ثانية بثانية
3. CTA في النهاية
4. الصوت/الموسيقى المقترحة
5. النص على الشاشة (text overlay)
6. الوصف + الهاشتاقات
7. أفضل وقت للنشر"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_series(self, theme, episodes=7):
        system = "صانع محتوى تيكتوك. صمم سلسلة محتوى تبني جمهور."
        return self.client.generate(
            f"صمم سلسلة تيكتوك من {episodes} حلقات عن: {theme}\nلكل حلقة: العنوان، الفكرة، Hook، المدة",
            system_prompt=system, max_tokens=2500
        )

    def generate_and_save(self, niche, **kw):
        content = self.generate(niche, **kw)
        return save_output(content, timestamp_filename(f"tiktok_{niche}", "md"), str(get_output_dir("content")))

def main():
    parser = argparse.ArgumentParser(description="TikTok Script Writer - كاتب سيناريو تيكتوك")
    parser.add_argument("--niche", "-n", required=True)
    parser.add_argument("--style", "-s", default="storytelling", choices=["storytelling", "educational", "comedy", "trending", "before_after"])
    parser.add_argument("--duration", "-d", type=int, default=60, choices=[15, 30, 60, 90])
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()
    writer = TikTokScriptWriter()
    if args.save:
        print(f"Saved to: {writer.generate_and_save(args.niche, style=args.style, duration=args.duration)}")
    else:
        print(writer.generate(args.niche, args.style, args.duration))

if __name__ == "__main__":
    main()
