"""AI-powered recipe creator for Saudi and international cuisines."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class RecipeCreator:
    """Create detailed, tested recipes with professional chef tips."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        cuisine: str,
        dietary: str = "",
        difficulty: str = "easy",
        servings: int = 4,
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a complete recipe.

        Args:
            cuisine: Type of cuisine or specific dish.
            dietary: Dietary restrictions (none/healthy/keto/vegan/gluten_free).
            difficulty: Difficulty level (easy/medium/hard).
            servings: Number of servings.
            language: Output language (default Arabic).

        Returns:
            Complete recipe as a string.
        """
        system = (
            "شيف محترف ومتخصص في المطبخ السعودي والعالمي. "
            "يكتب وصفات دقيقة ومجربة مع نصائح احترافية. "
            "يفهم التغذية والتكلفة. "
            "يقدم: اسم الطبق، الوصف، المقادير بالتفصيل، طريقة التحضير خطوة بخطوة، "
            "وقت التحضير والطبخ، السعرات، التكلفة التقديرية، نصائح الشيف، "
            "طريقة التقديم، اقتراح التصوير."
        )
        dietary_section = f"\nالنظام الغذائي: {dietary}" if dietary else ""
        prompt = (
            f"أنشئ وصفة طبخ كاملة واحترافية:\n\n"
            f"نوع المطبخ/الطبق: {cuisine}\n"
            f"مستوى الصعوبة: {difficulty}\n"
            f"عدد الحصص: {servings}{dietary_section}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل الوصفة:\n"
            f"- اسم الطبق ووصف مختصر شهي\n"
            f"- المقادير بالتفصيل مع الكميات الدقيقة\n"
            f"- طريقة التحضير خطوة بخطوة مرقمة\n"
            f"- وقت التحضير ووقت الطبخ والوقت الإجمالي\n"
            f"- السعرات الحرارية التقديرية لكل حصة\n"
            f"- التكلفة التقديرية\n"
            f"- نصائح الشيف للنجاح\n"
            f"- طريقة التقديم والتزيين\n"
            f"- اقتراحات للتصوير الاحترافي"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_from_ingredients(self, ingredients: str, **kw) -> str:
        """Generate a recipe based on available ingredients.

        Args:
            ingredients: Comma-separated list of available ingredients.

        Returns:
            Complete recipe using the provided ingredients.
        """
        system = (
            "شيف محترف ومتخصص في المطبخ السعودي والعالمي. "
            "يكتب وصفات دقيقة ومجربة مع نصائح احترافية. "
            "يبدع في ابتكار أطباق من المكونات المتاحة."
        )
        prompt = (
            f"ابتكر وصفة لذيذة باستخدام المكونات التالية:\n\n"
            f"المكونات المتاحة: {ingredients}\n\n"
            f"يجب أن تشمل الوصفة:\n"
            f"- اسم الطبق ووصف مختصر\n"
            f"- المقادير بالتفصيل مع الكميات\n"
            f"- طريقة التحضير خطوة بخطوة\n"
            f"- وقت التحضير والطبخ\n"
            f"- السعرات الحرارية التقديرية\n"
            f"- نصائح الشيف وبدائل المكونات"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_for_blog(self, recipe_name: str, with_seo: bool = True, **kw) -> str:
        """Generate a food blog post for a recipe.

        Args:
            recipe_name: Name of the recipe for the blog post.
            with_seo: Include SEO optimization (default True).

        Returns:
            Blog post content as a string.
        """
        system = (
            "شيف محترف ومتخصص في المطبخ السعودي والعالمي. "
            "يكتب وصفات دقيقة ومجربة مع نصائح احترافية. "
            "يكتب محتوى مدونات طعام جذاب ومحسّن لمحركات البحث."
        )
        seo_section = (
            "\n- تحسين العنوان والوصف لمحركات البحث (SEO)\n"
            "- كلمات مفتاحية مقترحة\n"
            "- وصف ميتا"
        ) if with_seo else ""
        prompt = (
            f"اكتب تدوينة طعام احترافية عن: {recipe_name}\n\n"
            f"يجب أن تشمل:\n"
            f"- عنوان جذاب\n"
            f"- مقدمة شخصية عن الطبق وقصته\n"
            f"- الوصفة الكاملة مع المقادير والخطوات\n"
            f"- نصائح وحيل الشيف\n"
            f"- أسئلة شائعة (FAQ)\n"
            f"- اقتراحات التصوير\n"
            f"- دعوة للتفاعل والمشاركة{seo_section}"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        cuisine: str,
        dietary: str = "",
        difficulty: str = "easy",
        servings: int = 4,
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a recipe and save it to a file."""
        content = self.generate(cuisine, dietary, difficulty, servings, language, **kw)
        return save_output(
            content,
            timestamp_filename("recipe", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="مبتكر الوصفات الذكي - وصفات احترافية من المطبخ السعودي والعالمي"
    )
    parser.add_argument("--cuisine", required=True, help="نوع المطبخ أو الطبق")
    parser.add_argument(
        "--dietary",
        choices=["none", "healthy", "keto", "vegan", "gluten_free"],
        default="",
        help="النظام الغذائي",
    )
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="easy",
        help="مستوى الصعوبة (افتراضي: easy)",
    )
    parser.add_argument("--servings", type=int, default=4, help="عدد الحصص (افتراضي: 4)")
    parser.add_argument("--save", action="store_true", help="حفظ الوصفة في ملف")

    args = parser.parse_args()
    gen = RecipeCreator()

    if args.save:
        path = gen.generate_and_save(args.cuisine, args.dietary, args.difficulty, args.servings)
        print(f"تم حفظ الوصفة في: {path}")
    else:
        print(gen.generate(args.cuisine, args.dietary, args.difficulty, args.servings))


if __name__ == "__main__":
    main()
