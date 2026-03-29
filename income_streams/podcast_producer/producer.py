"""AI Podcast Producer - Income Stream #19.
Business Model: إنتاج وتخطيط البودكاست بالذكاء الاصطناعي (200-800 ريال/شهر لكل بودكاست)
Usage: python -m income_streams.podcast_producer.producer --topic "الموضوع" --type interview --guest "اسم الضيف" --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class PodcastProducer:
    def __init__(self):
        self.client = AIClient(module_name="podcast_producer")

    def generate_episode_plan(self, topic: str, podcast_type: str = "interview", guest: str = "") -> str:
        system = (
            "أنت منتج بودكاست محترف بخبرة تزيد عن 8 سنوات في إنتاج المحتوى الصوتي العربي. "
            "تخطط حلقات جذابة تحافظ على اهتمام المستمع من البداية للنهاية. "
            "تكتب أسئلة مقابلات ذكية تستخرج قصصًا ومعلومات قيّمة من الضيوف. "
            "تصيغ show notes احترافية تجذب المستمعين الجدد وتحسّن ظهور البودكاست في محركات البحث. "
            "تفهم منصات البودكاست العربية (أنغامي، سبوتيفاي، أبل بودكاست) ومتطلبات كل منها. "
            "تعرف أسرار البودكاست الناجح: السرد القصصي، إيقاع الحلقة، والتفاعل مع الجمهور."
        )
        type_map = {
            "interview": "حلقة مقابلة مع ضيف",
            "solo": "حلقة فردية (مونولوج)",
            "panel": "حلقة نقاش جماعي (بانل)",
            "storytelling": "حلقة سرد قصصي"
        }
        type_desc = type_map.get(podcast_type, type_map["interview"])
        guest_section = f"\nالضيف: {guest}\nجهّز أسئلة مخصصة للضيف بناءً على خبراته ومجاله." if guest else ""
        prompt = (
            f"خطط حلقة بودكاست من نوع: {type_desc}\n"
            f"الموضوع: {topic}\n"
            f"{guest_section}\n\n"
            f"المطلوب بالتفصيل:\n\n"
            f"## 1. عنوان الحلقة\n"
            f"- 3 خيارات للعنوان (جذاب ومحسّن للبحث)\n\n"
            f"## 2. المقدمة (Hook) - أول 30 ثانية\n"
            f"- جملة افتتاحية تثير الفضول\n"
            f"- تقديم الموضوع وأهميته\n"
            f"- ما سيستفيده المستمع\n\n"
            f"## 3. النقاط الرئيسية\n"
            f"- 5-7 محاور رئيسية مع شرح كل محور\n"
            f"- ترتيب المحاور لتدرج منطقي\n\n"
            f"## 4. أسئلة المقابلة (إن وجد ضيف)\n"
            f"- 10-15 سؤال مرتب من العام للخاص\n"
            f"- أسئلة متابعة محتملة\n"
            f"- أسئلة شخصية/قصصية لإضفاء الحيوية\n\n"
            f"## 5. الختام\n"
            f"- ملخص أهم النقاط\n"
            f"- رسالة ختامية ملهمة\n"
            f"- CTA (تقييم، اشتراك، مشاركة)\n\n"
            f"## 6. Show Notes\n"
            f"- وصف الحلقة (150-200 كلمة)\n"
            f"- النقاط الرئيسية (bullet points)\n"
            f"- الروابط والمراجع المقترحة\n\n"
            f"## 7. الكلمات المفتاحية\n"
            f"- 10-15 كلمة مفتاحية للبحث\n\n"
            f"## 8. Timestamps\n"
            f"- تقسيم زمني تقريبي لكل جزء\n\n"
            f"## 9. CTA ووسائل التواصل\n"
            f"- نصوص جاهزة للترويج على السوشال ميديا (3 نصوص)\n"
            f"- اقتراحات مقاطع قصيرة للترويج"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_show_notes(self, episode_summary: str) -> str:
        system = (
            "أنت كاتب show notes محترف للبودكاست. تكتب ملاحظات حلقات جذابة ومحسّنة لمحركات البحث. "
            "تعرف كيف تلخص الحلقة بطريقة تشوّق المستمع الجديد وتفيد المستمع الحالي."
        )
        prompt = (
            f"اكتب Show Notes احترافية للحلقة التالية:\n{episode_summary}\n\n"
            f"المطلوب:\n"
            f"1. **العنوان المحسّن** (جذاب + SEO)\n"
            f"2. **الوصف القصير** (جملتان للمعاينة)\n"
            f"3. **الوصف الكامل** (150-200 كلمة)\n"
            f"4. **النقاط الرئيسية** (5-7 نقاط)\n"
            f"5. **Timestamps** مفصلة\n"
            f"6. **اقتباسات مميزة** من الحلقة (3-5 اقتباسات)\n"
            f"7. **الروابط والمراجع**\n"
            f"8. **الكلمات المفتاحية** (10-15)\n"
            f"9. **نصوص السوشال ميديا** (تويتر، إنستغرام، لينكدإن)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_series_plan(self, theme: str, episodes: int = 10) -> str:
        system = (
            "أنت مخطط محتوى بودكاست استراتيجي. تصمم سلاسل بودكاست متكاملة تبني جمهورًا وفيًا. "
            "تفهم كيفية ترتيب الحلقات لتحقيق نمو مستمر في عدد المستمعين."
        )
        prompt = (
            f"خطط سلسلة بودكاست متكاملة:\n"
            f"الموضوع العام: {theme}\n"
            f"عدد الحلقات: {episodes}\n\n"
            f"المطلوب:\n"
            f"1. **اسم السلسلة** (3 خيارات)\n"
            f"2. **وصف السلسلة** (فقرة تسويقية)\n"
            f"3. **الجمهور المستهدف**\n"
            f"4. **لكل حلقة**:\n"
            f"   - العنوان\n"
            f"   - الملخص (جملتان)\n"
            f"   - الضيف المقترح (نوع الخبرة المطلوبة)\n"
            f"   - 3 نقاط رئيسية\n"
            f"   - رابط الحلقة بالحلقة التالية\n"
            f"5. **خطة النشر** (التوقيت والتكرار)\n"
            f"6. **خطة الترويج**\n"
            f"7. **مؤشرات النجاح** (KPIs)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        content = self.generate_episode_plan(topic, **kwargs)
        return save_output(content, timestamp_filename("podcast", "md"), str(get_output_dir("reports")))


def main():
    parser = argparse.ArgumentParser(description="AI Podcast Producer - منتج البودكاست بالذكاء الاصطناعي")
    parser.add_argument("--topic", "-t", required=True, help="موضوع الحلقة أو السلسلة")
    parser.add_argument("--type", choices=["interview", "solo", "panel", "storytelling"], default="interview", help="نوع الحلقة")
    parser.add_argument("--guest", "-g", default="", help="اسم الضيف (اختياري)")
    parser.add_argument("--series", action="store_true", help="إنشاء خطة سلسلة كاملة بدلاً من حلقة واحدة")
    parser.add_argument("--save", "-s", action="store_true", help="حفظ الناتج في ملف")
    args = parser.parse_args()

    gen = PodcastProducer()

    if args.series:
        content = gen.generate_series_plan(args.topic)
    else:
        content = gen.generate_episode_plan(args.topic, podcast_type=args.type, guest=args.guest)

    if args.save:
        path = save_output(content, timestamp_filename("podcast", "md"), str(get_output_dir("reports")))
        print(f"Saved to: {path}")
    else:
        print(content)


if __name__ == "__main__":
    main()
