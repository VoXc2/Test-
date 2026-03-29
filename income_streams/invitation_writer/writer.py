"""AI-powered invitation writer for formal and informal events."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class InvitationWriter:
    """Write professional invitations following Saudi and Gulf protocol and etiquette."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        event_type: str,
        names: str = "",
        date: str = "",
        venue: str = "",
        style: str = "formal",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a professional invitation.

        Args:
            event_type: Type of event (wedding/conference/opening/dinner/graduation).
            names: Names of hosts or honorees.
            date: Event date.
            venue: Event venue.
            style: Writing style (formal/semi_formal/casual).
            language: Output language (default Arabic).

        Returns:
            Complete invitation text with variants.
        """
        system = (
            "كاتب دعوات محترف متخصص في الأسلوب العربي الرسمي والعصري. "
            "يكتب دعوات أعراس ومؤتمرات وافتتاحات بأسلوب أنيق. "
            "يقدم: نص الدعوة الرسمي، النسخة العصرية، نسخة واتساب، "
            "نسخة إنجليزية، RSVP message."
        )
        names_section = f"\nالأسماء: {names}" if names else ""
        date_section = f"\nالتاريخ: {date}" if date else ""
        venue_section = f"\nالمكان: {venue}" if venue else ""
        prompt = (
            f"اكتب دعوة احترافية للمناسبة التالية:\n\n"
            f"نوع المناسبة: {event_type}\n"
            f"الأسلوب: {style}{names_section}{date_section}{venue_section}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل:\n"
            f"- نص الدعوة الرسمي بالعربية الفصحى\n"
            f"- النسخة العصرية من الدعوة\n"
            f"- نسخة واتساب مختصرة وأنيقة\n"
            f"- نسخة إنجليزية رسمية\n"
            f"- رسالة RSVP (تأكيد الحضور)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_rsvp_message(self, event_type: str, **kw) -> str:
        """Generate RSVP message and response options for an event.

        Args:
            event_type: Type of event.

        Returns:
            RSVP message and response templates.
        """
        system = (
            "كاتب دعوات محترف متخصص في الأسلوب العربي الرسمي والعصري. "
            "يكتب دعوات أعراس ومؤتمرات وافتتاحات بأسلوب أنيق."
        )
        prompt = (
            f"أنشئ رسائل تأكيد حضور (RSVP) لـ: {event_type}\n\n"
            f"يشمل:\n"
            f"- نص بطاقة RSVP الرسمية\n"
            f"- رسالة تأكيد الحضور\n"
            f"- رسالة الاعتذار عن الحضور\n"
            f"- رسالة تأكيد عدد المرافقين\n"
            f"- رسالة تذكير بالمناسبة (قبل أسبوع/يوم)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        event_type: str,
        names: str = "",
        date: str = "",
        venue: str = "",
        style: str = "formal",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate an invitation and save it to a file."""
        content = self.generate(event_type, names, date, venue, style, language, **kw)
        return save_output(
            content,
            timestamp_filename("invitation", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="كاتب الدعوات الذكي - دعوات رسمية بالعربية والإنجليزية"
    )
    parser.add_argument(
        "--type",
        dest="event_type",
        required=True,
        choices=["wedding", "conference", "opening", "dinner", "graduation"],
        help="نوع المناسبة",
    )
    parser.add_argument("--names", required=True, help="أسماء المضيفين أو المحتفى بهم")
    parser.add_argument("--date", required=True, help="تاريخ المناسبة")
    parser.add_argument("--venue", default="", help="مكان المناسبة")
    parser.add_argument(
        "--style",
        choices=["formal", "modern", "casual"],
        default="formal",
        help="أسلوب الدعوة (افتراضي: formal)",
    )
    parser.add_argument("--language", default="ar", help="لغة الدعوة (افتراضي: ar)")
    parser.add_argument("--save", action="store_true", help="حفظ الدعوة في ملف")

    args = parser.parse_args()
    gen = InvitationWriter()

    if args.save:
        path = gen.generate_and_save(
            args.event_type, args.names, args.date, args.venue, args.style, args.language
        )
        print(f"تم حفظ الدعوة في: {path}")
    else:
        print(
            gen.generate(
                args.event_type, args.names, args.date, args.venue, args.style, args.language
            )
        )


if __name__ == "__main__":
    main()
