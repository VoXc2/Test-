"""AI Wellness Bot - Daily mental health check-ins and coping strategies.
Usage: python -m income_streams.wellness_bot.bot --mood "stressed" --type checkin
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class WellnessBot:
    """AI wellness companion for daily check-ins. NOT a substitute for professional help."""

    def __init__(self):
        self.client = AIClient()

    def daily_checkin(self, mood, energy_level="", stress_level="", language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"أنت مرشد صحة نفسية داعم وإيجابي. تقدم دعم يومي باستخدام تقنيات CBT والـ mindfulness. "
            f"تكتب بـ{lang}. تنويه مهم: أنت لست بديلاً عن المعالج النفسي المتخصص. "
            "كن دافئاً ومتعاطفاً، قدم تقنيات عملية قصيرة."
        )
        parts = [f"المزاج: {mood}"]
        if energy_level:
            parts.append(f"مستوى الطاقة: {energy_level}")
        if stress_level:
            parts.append(f"مستوى التوتر: {stress_level}")
        prompt = (
            "Check-in يومي:\n" + "\n".join(parts) + "\n\n"
            "قدم: 1. تأكيد وتطبيع المشاعر 2. تمرين تنفس (دقيقتين) "
            "3. نصيحة عملية لليوم 4. سؤال تأمل 5. تذكير إيجابي"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=1500)

    def coping_strategy(self, situation, language="ar"):
        system = "أنت مرشد صحة نفسية. قدم استراتيجيات تأقلم عملية وقصيرة. تنويه: لست بديلاً عن متخصص."
        prompt = f"الموقف: {situation}\n\nقدم 3-5 استراتيجيات تأقلم عملية يمكن تطبيقها فوراً."
        return self.client.generate(prompt, system_prompt=system, max_tokens=1500)

    def journal_prompt(self, theme="general", language="ar"):
        system = "أنت مرشد كتابة تأملية. اكتب أسئلة عميقة تساعد على التأمل الذاتي."
        return self.client.generate(f"اكتب 5 أسئلة journal prompts عن: {theme}", system_prompt=system, max_tokens=800)


def main():
    parser = argparse.ArgumentParser(description="Wellness Bot - بوت الصحة النفسية")
    parser.add_argument("--mood", "-m", required=True)
    parser.add_argument("--type", "-t", default="checkin", choices=["checkin", "coping", "journal"])
    parser.add_argument("--energy", "-e", default="")
    parser.add_argument("--stress", default="")
    args = parser.parse_args()
    bot = WellnessBot()
    if args.type == "checkin":
        print(bot.daily_checkin(args.mood, args.energy, args.stress))
    elif args.type == "coping":
        print(bot.coping_strategy(args.mood))
    else:
        print(bot.journal_prompt(args.mood))

if __name__ == "__main__":
    main()
