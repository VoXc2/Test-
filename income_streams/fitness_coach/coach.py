"""AI Fitness Coach - Income Stream.

Generates personalized workout programs and daily workout plans
based on goals, fitness level, and available equipment.

Business Model:
- Single workout plan: 30-80 SAR
- Monthly program: 100-300 SAR
- Premium coaching package: 300-800 SAR

Usage:
    python -m income_streams.fitness_coach.coach --goal muscle --level intermediate --equipment gym

تنويه: برامج تمرين عامة وليست بديلاً عن استشارة طبية أو مدرب شخصي معتمد.
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


GOALS_MAP = {
    "muscle": "بناء العضلات",
    "strength": "زيادة القوة",
    "cardio": "تحسين اللياقة القلبية",
    "flexibility": "تحسين المرونة",
    "weight_loss": "خسارة الوزن",
}

LEVELS_MAP = {
    "beginner": "مبتدئ",
    "intermediate": "متوسط",
    "advanced": "متقدم",
}

EQUIPMENT_MAP = {
    "gym": "صالة رياضية مجهزة بالكامل",
    "home": "معدات منزلية (دمبلز + بار + بنش)",
    "minimal": "بدون معدات (تمارين وزن الجسم فقط)",
}


class FitnessCoach:
    """AI-powered fitness program and workout generator."""

    def __init__(self):
        self.client = AIClient()

    def generate_program(
        self,
        goal: str,
        level: str = "intermediate",
        equipment: str = "gym",
        days_per_week: int = 4,
        language: str = "ar",
    ) -> str:
        """Generate a complete workout program.

        Args:
            goal: muscle, strength, cardio, flexibility, or weight_loss
            level: beginner, intermediate, or advanced
            equipment: gym, home, or minimal
            days_per_week: Training days per week (3-6)
            language: 'ar' or 'en'
        """
        goal_ar = GOALS_MAP.get(goal, goal)
        level_ar = LEVELS_MAP.get(level, level)
        equip_ar = EQUIPMENT_MAP.get(equipment, equipment)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "مدرب لياقة بدنية معتمد (NASM/ACE) متخصص في بناء برامج التمرين. "
            "يراعي مستوى المتدرب ومعداته المتاحة. "
            "يصمم برامج تدريبية علمية مبنية على مبادئ التدريب: "
            "التدرج في الحمل، التنويع، الراحة الكافية، والتخصصية. "
            "يهتم بالإحماء والتبريد ويقدم نصائح تغذية مناسبة للهدف.\n\n"
            "تنويه مهم: هذه برامج تمرين عامة وليست بديلاً عن استشارة طبية. "
            "استشر طبيبك قبل البدء بأي برنامج رياضي جديد."
        )

        prompt = (
            f"صمم برنامج تمرين أسبوعي كامل {lang}.\n\n"
            f"الهدف: {goal_ar}\n"
            f"المستوى: {level_ar}\n"
            f"المعدات: {equip_ar}\n"
            f"أيام التمرين: {days_per_week} أيام/أسبوع\n\n"
            "لكل يوم تمرين اذكر:\n"
            "1. العضلات المستهدفة\n"
            "2. الإحماء (5-10 دقائق)\n"
            "3. التمارين الرئيسية:\n"
            "   - اسم التمرين\n"
            "   - عدد المجموعات × التكرارات\n"
            "   - الراحة بين المجموعات\n"
            "   - ملاحظات الأداء الصحيح\n"
            "4. التبريد والإطالة (5-10 دقائق)\n\n"
            "أضف في النهاية:\n"
            "- جدول ملخص للأسبوع\n"
            "- نصائح التغذية المناسبة للهدف\n"
            "- نصائح الراحة والاستشفاء\n"
            "- متى يجب زيادة الأوزان/الشدة\n"
            "- تعديلات حسب التقدم\n\n"
            "تنويه: برنامج تمرين عام وليس بديلاً عن استشارة طبية أو مدرب شخصي معتمد."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_workout(
        self,
        muscle_group: str,
        duration: int = 45,
        language: str = "ar",
    ) -> str:
        """Generate a single workout session.

        Args:
            muscle_group: Target muscle group (chest, back, legs, shoulders, arms, core, full_body)
            duration: Workout duration in minutes
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "مدرب لياقة بدنية معتمد. يصمم جلسات تمرين فعالة ومتنوعة "
            "مع التركيز على الأداء الصحيح والسلامة.\n\n"
            "تنويه: تمارين عامة وليست بديلاً عن استشارة طبية."
        )

        prompt = (
            f"صمم جلسة تمرين واحدة {lang}.\n\n"
            f"العضلة المستهدفة: {muscle_group}\n"
            f"المدة: {duration} دقيقة\n\n"
            "اذكر:\n"
            "- الإحماء\n"
            "- التمارين (الاسم + المجموعات + التكرارات + الراحة)\n"
            "- نصائح الأداء الصحيح لكل تمرين\n"
            "- التبريد والإطالة\n"
            "- الأخطاء الشائعة التي يجب تجنبها"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_program_and_save(
        self,
        goal: str,
        level: str = "intermediate",
        equipment: str = "gym",
        days_per_week: int = 4,
        language: str = "ar",
    ) -> str:
        """Generate a fitness program and save it to file."""
        content = self.generate_program(
            goal, level=level, equipment=equipment,
            days_per_week=days_per_week, language=language,
        )
        return save_output(
            content,
            timestamp_filename("fitness_program", "md"),
            str(get_output_dir("fitness")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Fitness Coach - المدرب الرياضي الذكي"
    )
    parser.add_argument(
        "--goal",
        choices=["muscle", "strength", "cardio", "flexibility", "weight_loss"],
        default="muscle",
        help="Fitness goal",
    )
    parser.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate",
        help="Fitness level",
    )
    parser.add_argument(
        "--equipment",
        choices=["gym", "home", "minimal"],
        default="gym",
        help="Available equipment",
    )
    parser.add_argument(
        "--days", type=int, default=4, help="Training days per week (3-6)"
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    coach = FitnessCoach()

    if args.save:
        path = coach.generate_program_and_save(
            args.goal,
            level=args.level,
            equipment=args.equipment,
            days_per_week=args.days,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(
            coach.generate_program(
                args.goal,
                level=args.level,
                equipment=args.equipment,
                days_per_week=args.days,
                language=args.language,
            )
        )


if __name__ == "__main__":
    main()
