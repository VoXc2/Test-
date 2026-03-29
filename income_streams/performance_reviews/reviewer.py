"""AI Performance Review Writer - Income Stream.

Generates fair, constructive performance reviews with SMART goals
and development plans for employees.

Business Model:
- Single review: 50-150 SAR
- Department package: 300-1000 SAR
- Annual review cycle (enterprise): 2000-5000 SAR

Usage:
    python -m income_streams.performance_reviews.reviewer --name "أحمد" --role "مهندس برمجيات" --rating 4
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


RATING_MAP = {
    1: "أداء غير مقبول - يحتاج تحسين جذري",
    2: "أداء أقل من المتوقع - يحتاج تحسين",
    3: "أداء يلبي التوقعات - مقبول",
    4: "أداء يفوق التوقعات - ممتاز",
    5: "أداء استثنائي - متميز",
}


class PerformanceReviewWriter:
    """AI-powered performance review and development plan writer."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        employee_name: str,
        role: str,
        achievements: str = "",
        areas_to_improve: str = "",
        rating: int = 0,
        language: str = "ar",
    ) -> str:
        """Generate a comprehensive performance review.

        Args:
            employee_name: Employee's name
            role: Employee's job role
            achievements: Key achievements during the review period
            areas_to_improve: Areas that need improvement
            rating: Overall rating (1-5, 0 for auto)
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"
        rating_text = RATING_MAP.get(rating, "") if rating else ""

        system = (
            "مدير موارد بشرية خبير في إدارة الأداء مع 15+ سنة خبرة. "
            "يكتب تقييمات أداء عادلة وبناءة ومتوازنة. "
            "يضع أهداف SMART (محددة، قابلة للقياس، قابلة للتحقيق، ذات صلة، محددة بزمن). "
            "يصمم خطط تطوير واقعية ومحفزة. "
            "يستخدم لغة مهنية بناءة حتى في مجالات التحسين. "
            "يراعي ثقافة العمل السعودية والخليجية."
        )

        achievements_text = f"\nالإنجازات: {achievements}" if achievements else ""
        improve_text = f"\nمجالات التحسين: {areas_to_improve}" if areas_to_improve else ""
        rating_desc = f"\nالتقييم العام: {rating}/5 - {rating_text}" if rating else ""

        prompt = (
            f"اكتب تقييم أداء شامل ومهني {lang}.\n\n"
            f"اسم الموظف: {employee_name}\n"
            f"الدور الوظيفي: {role}\n"
            f"{achievements_text}{improve_text}{rating_desc}\n\n"
            "اكتب الأقسام التالية:\n\n"
            "## 1. ملخص الأداء العام\n"
            "فقرة شاملة تلخص أداء الموظف خلال الفترة\n\n"
            "## 2. الإنجازات والنقاط القوية\n"
            "- تفصيل الإنجازات مع أرقام وأمثلة\n"
            "- السلوكيات الإيجابية\n"
            "- المساهمات المميزة\n\n"
            "## 3. مجالات التحسين والتطوير\n"
            "- نقاط التحسين بلغة بناءة\n"
            "- اقتراحات محددة للتطوير\n\n"
            "## 4. أهداف SMART للفترة القادمة\n"
            "- 4-6 أهداف SMART واضحة\n"
            "- لكل هدف: المعيار + الموعد + مؤشر النجاح\n\n"
            "## 5. خطة التطوير الشخصي\n"
            "- الدورات والتدريبات المقترحة\n"
            "- المهارات المطلوب تطويرها\n"
            "- الموارد المتاحة\n"
            "- الجدول الزمني\n\n"
            "## 6. التقييم العام والتوصيات\n"
            "- التقييم النهائي\n"
            "- التوصيات (ترقية/زيادة/تدريب/تحسين)\n"
            "- تعليقات ختامية محفزة"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_development_plan(
        self,
        role: str,
        gaps: str,
        language: str = "ar",
    ) -> str:
        """Generate a personal development plan based on skill gaps.

        Args:
            role: Employee's job role
            gaps: Identified skill gaps or areas to develop
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير تطوير مهني متخصص في تصميم خطط التطوير الفردية. "
            "يربط الفجوات المهارية بالأهداف الوظيفية ويقترح مسارات تعلم واقعية."
        )

        prompt = (
            f"صمم خطة تطوير مهني شخصية {lang}.\n\n"
            f"الدور الوظيفي: {role}\n"
            f"الفجوات المهارية: {gaps}\n\n"
            "المطلوب:\n"
            "1. تحليل الفجوات وأولوياتها\n"
            "2. أهداف التطوير (قصيرة ومتوسطة وطويلة المدى)\n"
            "3. أنشطة التعلم المقترحة (دورات، كتب، مشاريع)\n"
            "4. جدول زمني (3-12 شهر)\n"
            "5. مقاييس النجاح لكل هدف\n"
            "6. نقاط المراجعة والمتابعة"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_smart_goals(
        self,
        role: str,
        focus_areas: str,
        language: str = "ar",
    ) -> str:
        """Generate SMART goals for an employee.

        Args:
            role: Employee's job role
            focus_areas: Areas to focus on for goal setting
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير إدارة أداء متخصص في وضع أهداف SMART. "
            "يضمن أن كل هدف محدد وقابل للقياس والتحقيق وذو صلة ومحدد بزمن."
        )

        prompt = (
            f"ضع أهداف SMART {lang} للدور التالي.\n\n"
            f"الدور: {role}\n"
            f"مجالات التركيز: {focus_areas}\n\n"
            "لكل هدف اذكر:\n"
            "- S (Specific): الهدف بوضوح\n"
            "- M (Measurable): كيف نقيس التحقق\n"
            "- A (Achievable): لماذا هو قابل للتحقيق\n"
            "- R (Relevant): صلته بالدور والأهداف العامة\n"
            "- T (Time-bound): الموعد النهائي\n\n"
            "ضع 5-7 أهداف SMART متنوعة تغطي:\n"
            "- الأداء الوظيفي\n"
            "- التطوير المهني\n"
            "- العمل الجماعي\n"
            "- الابتكار والتحسين"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_and_save(
        self,
        employee_name: str,
        role: str,
        achievements: str = "",
        areas_to_improve: str = "",
        rating: int = 0,
        language: str = "ar",
    ) -> str:
        """Generate a performance review and save it to file."""
        content = self.generate(
            employee_name, role,
            achievements=achievements,
            areas_to_improve=areas_to_improve,
            rating=rating, language=language,
        )
        return save_output(
            content,
            timestamp_filename("performance_review", "md"),
            str(get_output_dir("performance_reviews")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Performance Review Writer - كاتب تقييمات الأداء"
    )
    parser.add_argument(
        "--name", required=True, help="Employee name"
    )
    parser.add_argument(
        "--role", required=True, help="Employee role/title"
    )
    parser.add_argument(
        "--achievements", default="", help="Key achievements"
    )
    parser.add_argument(
        "--improve", default="", help="Areas to improve"
    )
    parser.add_argument(
        "--rating", type=int, default=0, choices=[0, 1, 2, 3, 4, 5],
        help="Overall rating (1-5, 0 for auto)",
    )
    parser.add_argument(
        "--type",
        choices=["review", "development", "goals"],
        default="review",
        help="Output type",
    )
    parser.add_argument(
        "--focus", default="", help="Focus areas for SMART goals"
    )
    parser.add_argument(
        "--gaps", default="", help="Skill gaps for development plan"
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    writer = PerformanceReviewWriter()

    if args.type == "development":
        print(writer.generate_development_plan(
            args.role, args.gaps or args.improve, language=args.language,
        ))
    elif args.type == "goals":
        print(writer.generate_smart_goals(
            args.role, args.focus or args.improve, language=args.language,
        ))
    elif args.save:
        path = writer.generate_and_save(
            args.name, args.role,
            achievements=args.achievements,
            areas_to_improve=args.improve,
            rating=args.rating,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(writer.generate(
            args.name, args.role,
            achievements=args.achievements,
            areas_to_improve=args.improve,
            rating=args.rating,
            language=args.language,
        ))


if __name__ == "__main__":
    main()
