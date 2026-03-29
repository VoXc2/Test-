"""AI Meal Planner - Income Stream.

Generates personalized meal plans with calorie tracking, macros,
and shopping lists tailored to Saudi/Gulf cuisine preferences.

Business Model:
- Basic meal plan: 30-80 SAR
- Monthly subscription: 100-300 SAR
- Customized plans with follow-up: 200-500 SAR

Usage:
    python -m income_streams.meal_planner.planner --goal weight_loss --calories 1800 --days 7

تنويه: خطط غذائية عامة وليست بديلاً عن استشارة أخصائي تغذية معتمد.
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


GOALS_MAP = {
    "weight_loss": "خسارة الوزن",
    "muscle_gain": "بناء العضلات",
    "maintenance": "الحفاظ على الوزن",
    "health": "تحسين الصحة العامة",
}


class MealPlanner:
    """AI-powered meal plan generator with Saudi/Gulf cuisine focus."""

    def __init__(self):
        self.client = AIClient()

    def generate_plan(
        self,
        goal: str,
        calories: int = 2000,
        restrictions: str = "",
        days: int = 7,
        language: str = "ar",
    ) -> str:
        """Generate a personalized meal plan.

        Args:
            goal: weight_loss, muscle_gain, maintenance, or health
            calories: Daily calorie target
            restrictions: Dietary restrictions (e.g., dairy-free, gluten-free)
            days: Number of days to plan
            language: 'ar' or 'en'
        """
        goal_ar = GOALS_MAP.get(goal, goal)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "أخصائي تغذية معتمد خبير في التغذية العلاجية والرياضية. "
            "يصمم خطط وجبات متوازنة تناسب الذوق السعودي والخليجي. "
            "يراعي الأكلات المحلية مثل الكبسة والمندي والجريش والمطبق والسليق. "
            "يحسب السعرات الحرارية والماكروز بدقة لكل وجبة. "
            "يقدم بدائل صحية للأطباق التقليدية عند الحاجة.\n\n"
            "تنويه مهم: هذه خطط غذائية عامة وليست بديلاً عن استشارة أخصائي تغذية معتمد."
        )

        restrictions_text = f"\nالقيود الغذائية: {restrictions}" if restrictions else ""

        prompt = (
            f"أنشئ خطة وجبات {lang} لمدة {days} أيام.\n\n"
            f"الهدف: {goal_ar}\n"
            f"السعرات اليومية المستهدفة: {calories} سعرة حرارية\n"
            f"{restrictions_text}\n\n"
            "المطلوب لكل يوم:\n"
            "1. الفطور - الوجبة + السعرات + الماكروز (بروتين/كارب/دهون)\n"
            "2. سناك الصباح\n"
            "3. الغداء - الوجبة + السعرات + الماكروز\n"
            "4. سناك العصر\n"
            "5. العشاء - الوجبة + السعرات + الماكروز\n\n"
            "أضف في النهاية:\n"
            "- إجمالي السعرات والماكروز لكل يوم\n"
            "- قائمة مشتريات أسبوعية مرتبة حسب الأقسام\n"
            "- نصائح للتحضير المسبق (meal prep)\n"
            "- بدائل للمكونات غير المتوفرة\n"
            "- نصائح عامة لتحقيق الهدف\n\n"
            "تنويه: هذه خطة غذائية عامة وليست بديلاً عن استشارة أخصائي تغذية معتمد."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_shopping_list(self, meal_plan: str, language: str = "ar") -> str:
        """Generate a detailed shopping list from a meal plan.

        Args:
            meal_plan: The meal plan text to extract shopping list from
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "أخصائي تغذية يساعد في تنظيم قوائم المشتريات. "
            "يرتب المشتريات حسب أقسام السوبرماركت لتسهيل التسوق."
        )

        prompt = (
            f"بناءً على خطة الوجبات التالية، أنشئ قائمة مشتريات مفصلة {lang}:\n\n"
            f"{meal_plan}\n\n"
            "رتب القائمة حسب الأقسام:\n"
            "- الخضروات والفواكه\n"
            "- اللحوم والدواجن والأسماك\n"
            "- الألبان والأجبان\n"
            "- الحبوب والبقوليات\n"
            "- البهارات والتوابل\n"
            "- المشروبات\n"
            "- أخرى\n\n"
            "اذكر الكميات المطلوبة لكل صنف."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_plan_and_save(
        self,
        goal: str,
        calories: int = 2000,
        restrictions: str = "",
        days: int = 7,
        language: str = "ar",
    ) -> str:
        """Generate a meal plan and save it to file."""
        content = self.generate_plan(
            goal, calories=calories, restrictions=restrictions,
            days=days, language=language,
        )
        return save_output(
            content,
            timestamp_filename("meal_plan", "md"),
            str(get_output_dir("meal_plans")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Meal Planner - مخطط الوجبات الذكي"
    )
    parser.add_argument(
        "--goal",
        choices=["weight_loss", "muscle_gain", "maintenance", "health"],
        default="health",
        help="Nutrition goal",
    )
    parser.add_argument(
        "--calories", type=int, default=2000, help="Daily calorie target"
    )
    parser.add_argument(
        "--restrictions", default="", help="Dietary restrictions"
    )
    parser.add_argument(
        "--days", type=int, default=7, help="Number of days to plan"
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    planner = MealPlanner()

    if args.save:
        path = planner.generate_plan_and_save(
            args.goal,
            calories=args.calories,
            restrictions=args.restrictions,
            days=args.days,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(
            planner.generate_plan(
                args.goal,
                calories=args.calories,
                restrictions=args.restrictions,
                days=args.days,
                language=args.language,
            )
        )


if __name__ == "__main__":
    main()
