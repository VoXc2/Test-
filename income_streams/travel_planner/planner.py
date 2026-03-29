"""AI-powered travel planner with detailed daily itineraries and budgets."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class TravelPlanner:
    """Design comprehensive travel plans with daily itineraries, budgets, and recommendations."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        destination: str,
        days: int,
        budget: str = "medium",
        travelers: int = 2,
        interests: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a detailed travel plan.

        Args:
            destination: Travel destination.
            days: Number of days.
            budget: Budget level (budget/medium/luxury).
            travelers: Number of travelers.
            interests: Specific interests or activities.
            language: Output language (default Arabic).

        Returns:
            Complete travel plan as a string.
        """
        system = (
            "مستشار سفر خبير ومرشد سياحي معتمد. "
            "يصمم خطط سفر مفصلة يومياً مع ميزانية واقعية. "
            "يعرف أفضل الأماكن والمطاعم والتجارب في كل وجهة. "
            "يقدم: نظرة عامة على الوجهة، خطة يومية مفصلة (صباح/ظهر/مساء)، "
            "الفنادق المقترحة (3 مستويات)، المطاعم، وسائل النقل، "
            "الميزانية التفصيلية، نصائح مهمة، الطقس المتوقع، تطبيقات مفيدة."
        )
        interests_section = f"\nالاهتمامات: {interests}" if interests else ""
        prompt = (
            f"صمم خطة سفر مفصلة:\n\n"
            f"الوجهة: {destination}\n"
            f"عدد الأيام: {days}\n"
            f"مستوى الميزانية: {budget}\n"
            f"عدد المسافرين: {travelers}{interests_section}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل الخطة:\n"
            f"- نظرة عامة على الوجهة (معلومات أساسية)\n"
            f"- خطة يومية مفصلة لكل يوم (صباح/ظهر/مساء)\n"
            f"- اقتراحات فنادق (3 مستويات: اقتصادي/متوسط/فاخر)\n"
            f"- أفضل المطاعم المقترحة\n"
            f"- وسائل النقل والتنقل\n"
            f"- ميزانية تفصيلية (إقامة/طعام/تنقل/أنشطة)\n"
            f"- نصائح مهمة للمسافر\n"
            f"- الطقس المتوقع وماذا تحزم\n"
            f"- تطبيقات مفيدة للرحلة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_daily_itinerary(
        self,
        destination: str,
        day_number: int,
        **kw,
    ) -> str:
        """Generate a detailed itinerary for a specific day.

        Args:
            destination: Travel destination.
            day_number: The day number to plan.

        Returns:
            Detailed daily itinerary as a string.
        """
        system = (
            "خبير سفر ومرشد سياحي محترف. "
            "يصمم رحلات مفصلة تشمل كل التفاصيل العملية. "
            "يعرف الأسعار والمواسم وأفضل الأماكن."
        )
        prompt = (
            f"صمم جدولاً تفصيلياً لليوم {day_number} في {destination}:\n\n"
            f"يجب أن يشمل:\n"
            f"- برنامج الصباح (8:00-12:00): الأماكن والأنشطة\n"
            f"- برنامج الظهر (12:00-16:00): الغداء والأنشطة\n"
            f"- برنامج المساء (16:00-22:00): العشاء والسهرة\n"
            f"- تكلفة تقديرية لكل نشاط\n"
            f"- وسائل التنقل بين الأماكن\n"
            f"- نصائح عملية لهذا اليوم\n"
            f"- بدائل في حالة الطقس السيئ"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        destination: str,
        days: int,
        budget: str = "medium",
        travelers: int = 2,
        interests: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a travel plan and save it to a file."""
        content = self.generate(destination, days, budget, travelers, interests, language, **kw)
        return save_output(
            content,
            timestamp_filename("travel_plan", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="مخطط السفر الذكي - خطط سفر مفصلة مع ميزانيات واقعية"
    )
    parser.add_argument("--destination", required=True, help="وجهة السفر")
    parser.add_argument("--days", type=int, required=True, help="عدد أيام الرحلة")
    parser.add_argument(
        "--budget",
        choices=["budget", "medium", "luxury"],
        default="medium",
        help="مستوى الميزانية (افتراضي: medium)",
    )
    parser.add_argument("--travelers", type=int, default=2, help="عدد المسافرين (افتراضي: 2)")
    parser.add_argument("--interests", default="", help="اهتمامات وأنشطة مفضلة")
    parser.add_argument("--save", action="store_true", help="حفظ الخطة في ملف")

    args = parser.parse_args()
    gen = TravelPlanner()

    if args.save:
        path = gen.generate_and_save(
            args.destination, args.days, args.budget, args.travelers, args.interests
        )
        print(f"تم حفظ خطة السفر في: {path}")
    else:
        print(
            gen.generate(
                args.destination, args.days, args.budget, args.travelers, args.interests
            )
        )


if __name__ == "__main__":
    main()
