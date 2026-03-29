"""AI-powered restaurant menu designer using menu engineering principles."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class MenuDesigner:
    """Design optimized restaurant menus using menu engineering and pricing psychology."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        restaurant_type: str,
        items_count: int = 30,
        strategy: str = "profit_maximization",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a complete restaurant menu.

        Args:
            restaurant_type: Type/cuisine of the restaurant.
            items_count: Number of menu items to include.
            strategy: Pricing strategy (profit_maximization/value/premium).
            language: Output language (default Arabic).

        Returns:
            Complete menu design as a string.
        """
        system = (
            "خبير هندسة قوائم الطعام (Menu Engineering) ومستشار مطاعم. "
            "يصمم قوائم تزيد متوسط الفاتورة 20-30%. "
            "يفهم سيكولوجية التسعير والعين المتجولة. "
            "يقدم: أقسام القائمة، الأطباق (اسم جذاب + وصف شهي + سعر ذكي)، "
            "الأطباق النجمة (Star items)، استراتيجية التسعير، "
            "توصيات التصميم البصري، العناصر الترويجية."
        )
        prompt = (
            f"صمم قائمة طعام احترافية للمطعم التالي:\n\n"
            f"نوع المطعم: {restaurant_type}\n"
            f"عدد الأطباق: {items_count}\n"
            f"استراتيجية التسعير: {strategy}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل القائمة:\n"
            f"- أقسام مرتبة (مقبلات، أطباق رئيسية، حلويات، مشروبات)\n"
            f"- لكل طبق: اسم جذاب + وصف شهي + سعر ذكي\n"
            f"- تحديد الأطباق النجمة (Star Items) الأكثر ربحية\n"
            f"- استراتيجية التسعير النفسي\n"
            f"- توصيات التصميم البصري وترتيب العناصر\n"
            f"- عناصر ترويجية (وجبات كومبو، عروض خاصة)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def optimize_menu(self, current_menu: str, **kw) -> str:
        """Optimize an existing menu for better profitability.

        Args:
            current_menu: The current menu content to optimize.

        Returns:
            Optimization recommendations as a string.
        """
        system = (
            "خبير هندسة قوائم الطعام (Menu Engineering) ومستشار مطاعم. "
            "يصمم قوائم تزيد متوسط الفاتورة 20-30%. "
            "يفهم سيكولوجية التسعير والعين المتجولة."
        )
        prompt = (
            f"حلل وحسّن قائمة الطعام التالية:\n\n"
            f"{current_menu}\n\n"
            f"قدم:\n"
            f"- تحليل نقاط القوة والضعف\n"
            f"- تصنيف الأطباق (Stars/Puzzles/Plowhorses/Dogs)\n"
            f"- توصيات تحسين الأسعار\n"
            f"- اقتراحات إعادة ترتيب العناصر\n"
            f"- أطباق يجب حذفها أو تعديلها\n"
            f"- أفكار أطباق جديدة مقترحة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_descriptions(self, items: str, **kw) -> str:
        """Generate appetizing descriptions for menu items.

        Args:
            items: Comma-separated list of dish names.

        Returns:
            Appetizing descriptions for all items as a string.
        """
        system = (
            "خبير هندسة قوائم الطعام (Menu Engineering) ومستشار مطاعم. "
            "يكتب أوصاف أطباق شهية تثير الرغبة في الطلب وتزيد المبيعات."
        )
        prompt = (
            f"اكتب أوصافاً شهية وجذابة للأطباق التالية:\n\n"
            f"{items}\n\n"
            f"لكل طبق اكتب وصفاً من 2-3 أسطر يثير الحواس ويذكر المكونات الرئيسية "
            f"وطريقة التحضير بأسلوب تسويقي جذاب."
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        restaurant_type: str,
        items_count: int = 30,
        strategy: str = "profit_maximization",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a menu and save it to a file."""
        content = self.generate(restaurant_type, items_count, strategy, language, **kw)
        return save_output(
            content,
            timestamp_filename("menu", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="مصمم قوائم الطعام الذكي - هندسة القوائم وسيكولوجية التسعير"
    )
    parser.add_argument("--restaurant", required=True, help="نوع المطعم")
    parser.add_argument("--items", type=int, default=30, help="عدد الأطباق (افتراضي: 30)")
    parser.add_argument(
        "--strategy",
        choices=["profit", "value", "premium"],
        default="profit",
        help="استراتيجية التسعير (افتراضي: profit)",
    )
    parser.add_argument("--language", default="ar", help="لغة القائمة (افتراضي: ar)")
    parser.add_argument("--save", action="store_true", help="حفظ القائمة في ملف")

    args = parser.parse_args()
    gen = MenuDesigner()

    strategy_map = {"profit": "profit_maximization", "value": "value", "premium": "premium"}
    strategy = strategy_map.get(args.strategy, args.strategy)

    if args.save:
        path = gen.generate_and_save(args.restaurant, args.items, strategy, args.language)
        print(f"تم حفظ القائمة في: {path}")
    else:
        print(gen.generate(args.restaurant, args.items, strategy, args.language))


if __name__ == "__main__":
    main()
