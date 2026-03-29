"""AI-powered event planner for conferences, weddings, exhibitions, and corporate events."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class EventPlanner:
    """Plan professional events with detailed timelines, budgets, and logistics."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        event_type: str,
        attendees: int,
        budget: float,
        location: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a comprehensive event plan.

        Args:
            event_type: Type of event (conference/wedding/exhibition/corporate/launch).
            attendees: Expected number of attendees.
            budget: Total budget available.
            location: Event location.
            language: Output language (default Arabic).

        Returns:
            Complete event plan as a string.
        """
        system = (
            "مخطط فعاليات محترف معتمد (CMP) خبير في تنظيم الفعاليات في السعودية. "
            "يخطط من المؤتمرات للأعراس للمعارض. "
            "يقدم: ملخص الفعالية، الجدول الزمني التفصيلي، الميزانية التفصيلية، "
            "قائمة الموردين، قائمة المهام (قبل بشهر/أسبوع/يوم)، خطة الطوارئ، "
            "الديكور والتصميم، التقنيات المطلوبة."
        )
        location_section = f"\nالموقع: {location}" if location else ""
        prompt = (
            f"أنشئ خطة تنظيم فعالية شاملة:\n\n"
            f"نوع الفعالية: {event_type}\n"
            f"عدد الحضور المتوقع: {attendees}\n"
            f"الميزانية: {budget} ريال{location_section}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل الخطة:\n"
            f"- ملخص الفعالية (الرؤية والأهداف)\n"
            f"- الجدول الزمني التفصيلي (من البداية للنهاية)\n"
            f"- الميزانية التفصيلية (المكان، الضيافة، التقنيات، الديكور، التسويق، الطوارئ)\n"
            f"- قائمة الموردين المقترحين (كاترينج، صوتيات، تصوير، ديكور)\n"
            f"- قائمة المهام (قبل بشهر، قبل بأسبوع، يوم الفعالية)\n"
            f"- خطة الطوارئ والبدائل\n"
            f"- الديكور والتصميم المقترح\n"
            f"- التقنيات والمعدات المطلوبة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_timeline(self, event_type: str, date: str, **kw) -> str:
        """Generate a detailed event timeline.

        Args:
            event_type: Type of event.
            date: Event date.

        Returns:
            Detailed timeline as a string.
        """
        system = (
            "مخطط فعاليات محترف معتمد (CMP) خبير في تنظيم الفعاليات في السعودية. "
            "يخطط من المؤتمرات للأعراس للمعارض."
        )
        prompt = (
            f"أنشئ جدولاً زمنياً تفصيلياً للفعالية التالية:\n\n"
            f"نوع الفعالية: {event_type}\n"
            f"التاريخ: {date}\n\n"
            f"يجب أن يشمل الجدول:\n"
            f"- التحضيرات قبل الفعالية (شهر/أسبوع/يوم)\n"
            f"- برنامج يوم الفعالية بالساعة والدقيقة\n"
            f"- فترات الاستراحة والضيافة\n"
            f"- أنشطة ما بعد الفعالية\n"
            f"- المسؤوليات لكل فترة زمنية"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_vendor_list(self, event_type: str, location: str, **kw) -> str:
        """Generate a recommended vendor list for an event.

        Args:
            event_type: Type of event.
            location: Event location or city.

        Returns:
            Categorized vendor recommendations as a string.
        """
        system = (
            "مخطط فعاليات محترف معتمد (CMP) خبير في تنظيم الفعاليات في السعودية. "
            "يعرف أفضل الموردين وشركات الخدمات في المملكة."
        )
        prompt = (
            f"أنشئ قائمة موردين مقترحة للفعالية التالية:\n\n"
            f"نوع الفعالية: {event_type}\n"
            f"الموقع: {location}\n\n"
            f"يجب أن تشمل القائمة:\n"
            f"- شركات تجهيز المكان والأثاث\n"
            f"- خدمات الضيافة والكاترينج\n"
            f"- شركات الصوت والإضاءة\n"
            f"- خدمات التصوير والفيديو\n"
            f"- شركات الديكور والزهور\n"
            f"- خدمات الطباعة والهدايا\n"
            f"- شركات الأمن والسلامة\n"
            f"- لكل مورد: الخدمات، نطاق الأسعار، ملاحظات"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        event_type: str,
        attendees: int,
        budget: float,
        location: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate an event plan and save it to a file."""
        content = self.generate(event_type, attendees, budget, location, language, **kw)
        return save_output(
            content,
            timestamp_filename("event_plan", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="منظم الفعاليات الذكي - تخطيط شامل للمؤتمرات والحفلات والمعارض"
    )
    parser.add_argument(
        "--type",
        dest="event_type",
        required=True,
        choices=["conference", "wedding", "exhibition", "corporate", "launch"],
        help="نوع الفعالية",
    )
    parser.add_argument("--attendees", type=int, required=True, help="عدد الحضور المتوقع")
    parser.add_argument("--budget", type=float, required=True, help="الميزانية بالريال")
    parser.add_argument("--location", default="", help="موقع الفعالية")
    parser.add_argument("--save", action="store_true", help="حفظ الخطة في ملف")

    args = parser.parse_args()
    gen = EventPlanner()

    if args.save:
        path = gen.generate_and_save(
            args.event_type, args.attendees, args.budget, args.location
        )
        print(f"تم حفظ خطة الفعالية في: {path}")
    else:
        print(gen.generate(args.event_type, args.attendees, args.budget, args.location))


if __name__ == "__main__":
    main()
