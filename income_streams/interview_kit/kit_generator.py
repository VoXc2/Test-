"""AI Interview Kit Generator - Income Stream.

Generates comprehensive interview question kits with scoring rubrics,
expected answers, and candidate evaluation templates.

Business Model:
- Single interview kit: 100-300 SAR
- Department package: 500-1500 SAR
- Enterprise subscription: 1000-3000 SAR/month

Usage:
    python -m income_streams.interview_kit.kit_generator --position "مهندس برمجيات" --level senior
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


LEVELS_MAP = {
    "junior": "مبتدئ",
    "mid": "متوسط الخبرة",
    "senior": "خبير",
    "lead": "قائد فريق",
    "executive": "تنفيذي",
}

FOCUS_MAP = {
    "technical": "تقنية",
    "behavioral": "سلوكية",
    "mixed": "مختلطة (تقنية + سلوكية)",
}


class InterviewKitGenerator:
    """AI-powered interview kit and scoring rubric generator."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        position: str,
        level: str = "senior",
        focus: str = "mixed",
        num_questions: int = 15,
        language: str = "ar",
    ) -> str:
        """Generate a complete interview question kit.

        Args:
            position: Job position to interview for
            level: junior, mid, senior, lead, or executive
            focus: technical, behavioral, or mixed
            num_questions: Number of questions to generate
            language: 'ar' or 'en'
        """
        level_ar = LEVELS_MAP.get(level, level)
        focus_ar = FOCUS_MAP.get(focus, focus)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير توظيف ومقابلات مع 10+ سنوات خبرة في الشركات الكبرى. "
            "يصمم أسئلة مقابلات تكشف الكفاءات الحقيقية للمرشحين. "
            "يستخدم أساليب STAR (Situation, Task, Action, Result) "
            "و behavioral interviewing و competency-based interviewing. "
            "يراعي الثقافة المحلية السعودية والخليجية في صياغة الأسئلة. "
            "يصمم معايير تقييم واضحة وعادلة لضمان موضوعية المقابلة."
        )

        prompt = (
            f"صمم حقيبة مقابلة وظيفية شاملة {lang}.\n\n"
            f"الوظيفة: {position}\n"
            f"المستوى: {level_ar}\n"
            f"نوع الأسئلة: {focus_ar}\n"
            f"عدد الأسئلة: {num_questions}\n\n"
            "المطلوب:\n\n"
            "## أولاً: أسئلة تقنية\n"
            "- أسئلة تختبر المعرفة التقنية والمهارات العملية\n"
            "- لكل سؤال: السؤال + الإجابة المتوقعة + معايير التقييم (1-5)\n\n"
            "## ثانياً: أسئلة سلوكية (STAR)\n"
            "- أسئلة تكشف السلوكيات والكفاءات\n"
            "- لكل سؤال: السؤال + ما نبحث عنه + red flags\n\n"
            "## ثالثاً: أسئلة مواقف (Situational)\n"
            "- سيناريوهات واقعية لتقييم التفكير\n"
            "- لكل سؤال: الموقف + الإجابة المثالية\n\n"
            "## رابعاً: ألغاز وأسئلة تحليلية\n"
            "- أسئلة تختبر التفكير النقدي وحل المشكلات\n\n"
            "## خامساً: نموذج تقييم المرشح\n"
            "- جدول تقييم شامل بمعايير واضحة\n"
            "- مقياس 1-5 لكل كفاءة\n"
            "- ملاحظات وتوصيات\n"
            "- قرار نهائي (مقبول/مرفوض/قائمة انتظار)"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_scoring_rubric(
        self,
        position: str,
        language: str = "ar",
    ) -> str:
        """Generate a scoring rubric for interview evaluation.

        Args:
            position: Job position
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير موارد بشرية متخصص في تصميم نماذج تقييم المرشحين. "
            "يضمن العدالة والموضوعية في عملية التقييم."
        )

        prompt = (
            f"صمم نموذج تقييم مقابلة (scoring rubric) {lang} لوظيفة: {position}\n\n"
            "يتضمن:\n"
            "1. الكفاءات الأساسية المطلوبة (5-8 كفاءات)\n"
            "2. وصف كل مستوى (1-5) لكل كفاءة\n"
            "3. الوزن النسبي لكل كفاءة\n"
            "4. الحد الأدنى المقبول\n"
            "5. نموذج ملاحظات المقابِل\n"
            "6. قسم التوصية النهائية"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_and_save(
        self,
        position: str,
        level: str = "senior",
        focus: str = "mixed",
        num_questions: int = 15,
        language: str = "ar",
    ) -> str:
        """Generate an interview kit and save it to file."""
        content = self.generate(
            position, level=level, focus=focus,
            num_questions=num_questions, language=language,
        )
        return save_output(
            content,
            timestamp_filename("interview_kit", "md"),
            str(get_output_dir("interview_kits")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Interview Kit Generator - مولّد حقيبة المقابلات"
    )
    parser.add_argument(
        "--position", required=True, help="Job position"
    )
    parser.add_argument(
        "--level",
        choices=["junior", "mid", "senior", "lead", "executive"],
        default="senior",
        help="Seniority level",
    )
    parser.add_argument(
        "--focus",
        choices=["technical", "behavioral", "mixed"],
        default="mixed",
        help="Question focus type",
    )
    parser.add_argument(
        "--questions", type=int, default=15, help="Number of questions"
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = InterviewKitGenerator()

    if args.save:
        path = gen.generate_and_save(
            args.position,
            level=args.level,
            focus=args.focus,
            num_questions=args.questions,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(gen.generate(
            args.position,
            level=args.level,
            focus=args.focus,
            num_questions=args.questions,
            language=args.language,
        ))


if __name__ == "__main__":
    main()
