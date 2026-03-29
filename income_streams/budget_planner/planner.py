"""AI-powered budget planner for personal and business financial planning."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class BudgetPlanner:
    """Generate comprehensive budget plans following the 50/30/20 rule and smart financial planning."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        income: float,
        budget_type: str = "personal",
        goals: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a comprehensive budget plan.

        Args:
            income: Monthly income amount.
            budget_type: Type of budget (personal/business/project).
            goals: Financial goals description.
            language: Output language (default Arabic).

        Returns:
            Detailed budget plan as a string.
        """
        system = (
            "مستشار مالي معتمد (CFP) خبير في التخطيط المالي الشخصي والمؤسسي. "
            "يتبع قاعدة 50/30/20 والتخطيط المالي الذكي. "
            "يقدم خطة شاملة تشمل: توزيع الدخل، فئات المصروفات مع النسب، "
            "خطة الادخار، خطة الاستثمار، صندوق الطوارئ، نصائح تقليل المصروفات، "
            "أهداف مالية قصيرة وطويلة المدى."
        )
        goals_section = f"\nالأهداف المالية: {goals}" if goals else ""
        prompt = (
            f"أنشئ خطة ميزانية شاملة بالتفاصيل التالية:\n\n"
            f"الدخل الشهري: {income} ريال\n"
            f"نوع الميزانية: {budget_type}\n"
            f"اللغة: {language}{goals_section}\n\n"
            f"يجب أن تشمل الخطة:\n"
            f"- توزيع الدخل حسب قاعدة 50/30/20\n"
            f"- فئات المصروفات التفصيلية مع النسب والمبالغ\n"
            f"- خطة ادخار شهرية وسنوية\n"
            f"- خطة استثمار مقترحة\n"
            f"- صندوق طوارئ (3-6 أشهر)\n"
            f"- نصائح عملية لتقليل المصروفات\n"
            f"- أهداف مالية قصيرة المدى (3-12 شهر) وطويلة المدى (1-5 سنوات)"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_project_budget(
        self,
        project_description: str,
        total_budget: float,
        **kw,
    ) -> str:
        """Generate a project-specific budget breakdown.

        Args:
            project_description: Description of the project.
            total_budget: Total available budget for the project.

        Returns:
            Project budget breakdown as a string.
        """
        system = (
            "مستشار مالي معتمد (CFP) خبير في التخطيط المالي الشخصي والمؤسسي. "
            "يتبع قاعدة 50/30/20 والتخطيط المالي الذكي. "
            "متخصص في إعداد ميزانيات المشاريع وتوزيع التكاليف."
        )
        prompt = (
            f"أنشئ ميزانية تفصيلية للمشروع التالي:\n\n"
            f"وصف المشروع: {project_description}\n"
            f"الميزانية الإجمالية: {total_budget} ريال\n\n"
            f"يجب أن تشمل:\n"
            f"- توزيع الميزانية على مراحل المشروع\n"
            f"- تكاليف الموارد البشرية\n"
            f"- تكاليف التقنية والأدوات\n"
            f"- تكاليف التسويق والمبيعات\n"
            f"- احتياطي الطوارئ (10-15%)\n"
            f"- جدول التدفقات النقدية المتوقعة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        income: float,
        budget_type: str = "personal",
        goals: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a budget plan and save it to a file."""
        content = self.generate(income, budget_type, goals, language, **kw)
        return save_output(
            content,
            timestamp_filename("budget", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="مخطط الميزانية الذكي - تخطيط مالي شخصي ومؤسسي"
    )
    parser.add_argument("--income", type=float, required=True, help="الدخل الشهري بالريال")
    parser.add_argument(
        "--type",
        dest="budget_type",
        choices=["personal", "business", "project"],
        default="personal",
        help="نوع الميزانية (افتراضي: personal)",
    )
    parser.add_argument("--goals", default="", help="الأهداف المالية")
    parser.add_argument("--save", action="store_true", help="حفظ الخطة في ملف")

    args = parser.parse_args()
    gen = BudgetPlanner()

    if args.save:
        path = gen.generate_and_save(args.income, args.budget_type, args.goals)
        print(f"تم حفظ خطة الميزانية في: {path}")
    else:
        print(gen.generate(args.income, args.budget_type, args.goals))


if __name__ == "__main__":
    main()
