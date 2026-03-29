"""AI Onboarding Plan Generator - Income Stream.

Generates comprehensive 30/60/90-day onboarding plans for new employees,
including weekly checklists, meetings, goals, and success criteria.

Business Model:
- Single onboarding plan: 100-300 SAR
- Department package: 500-1500 SAR
- Enterprise template library: 1000-3000 SAR

Usage:
    python -m income_streams.onboarding_generator.generator --role "مهندس برمجيات" --department "التقنية"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


COMPANY_SIZE_MAP = {
    "small": "شركة صغيرة (أقل من 50 موظف)",
    "medium": "شركة متوسطة (50-500 موظف)",
    "large": "شركة كبيرة (أكثر من 500 موظف)",
}


class OnboardingGenerator:
    """AI-powered employee onboarding plan generator."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        role: str,
        department: str = "",
        company_size: str = "medium",
        language: str = "ar",
    ) -> str:
        """Generate a complete onboarding plan.

        Args:
            role: Job role/title
            department: Department name
            company_size: small, medium, or large
            language: 'ar' or 'en'
        """
        size_ar = COMPANY_SIZE_MAP.get(company_size, company_size)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير تهيئة الموظفين الجدد ومتخصص في تجربة الموظف (Employee Experience). "
            "يصمم خطط onboarding تقلل وقت الوصول للإنتاجية وتزيد نسبة الاحتفاظ بالموظفين. "
            "يراعي الثقافة التنظيمية السعودية والخليجية. "
            "يدمج أفضل الممارسات العالمية مع الواقع المحلي. "
            "يهتم بالجوانب الإدارية والتقنية والاجتماعية والثقافية."
        )

        dept_text = f"\nالقسم: {department}" if department else ""

        prompt = (
            f"صمم خطة تهيئة موظف جديد (onboarding) شاملة {lang}.\n\n"
            f"الدور الوظيفي: {role}\n"
            f"{dept_text}\n"
            f"حجم الشركة: {size_ar}\n\n"
            "## خطة 30/60/90 يوم:\n\n"
            "### الأسبوع الأول (أيام 1-5):\n"
            "- قائمة مهام يومية مفصلة\n"
            "- الاجتماعات المطلوبة مع من\n"
            "- المعرفة الأساسية المطلوبة\n\n"
            "### الشهر الأول (أيام 1-30):\n"
            "- الأهداف المطلوب تحقيقها\n"
            "- المهام الأسبوعية\n"
            "- الاجتماعات الدورية\n"
            "- موارد التعلم والتدريب\n\n"
            "### الشهر الثاني (أيام 31-60):\n"
            "- أهداف متقدمة\n"
            "- مشاريع مستقلة\n"
            "- تقييم منتصف الفترة\n\n"
            "### الشهر الثالث (أيام 61-90):\n"
            "- أهداف الإنتاجية الكاملة\n"
            "- المساهمة المستقلة\n"
            "- تقييم نهاية فترة التجربة\n\n"
            "أضف أيضاً:\n"
            "- قائمة الأدوات والأنظمة المطلوب الوصول لها\n"
            "- دليل الزملاء الرئيسيين (buddy system)\n"
            "- معايير نجاح فترة التجربة\n"
            "- نموذج التقييم الشهري\n"
            "- نصائح للمدير المباشر"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_checklist(
        self,
        role: str,
        week: int = 1,
        language: str = "ar",
    ) -> str:
        """Generate a weekly onboarding checklist.

        Args:
            role: Job role/title
            week: Week number (1-12)
            language: 'ar' or 'en'
        """
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير تهيئة موظفين متخصص في تصميم قوائم المهام الأسبوعية. "
            "يضمن تغطية جميع الجوانب الإدارية والتقنية والاجتماعية."
        )

        prompt = (
            f"أنشئ قائمة مهام (checklist) {lang} للأسبوع {week} من تهيئة موظف جديد.\n\n"
            f"الدور: {role}\n\n"
            "لكل مهمة اذكر:\n"
            "- [ ] وصف المهمة\n"
            "- المسؤول عن تنفيذها (الموظف/المدير/HR)\n"
            "- الوقت المتوقع\n"
            "- الأولوية (عالية/متوسطة/منخفضة)\n\n"
            "قسّم المهام إلى:\n"
            "1. مهام إدارية\n"
            "2. مهام تقنية/مهنية\n"
            "3. مهام اجتماعية وثقافية\n"
            "4. مهام تعلّم وتطوير"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_and_save(
        self,
        role: str,
        department: str = "",
        company_size: str = "medium",
        language: str = "ar",
    ) -> str:
        """Generate an onboarding plan and save it to file."""
        content = self.generate(
            role, department=department,
            company_size=company_size, language=language,
        )
        return save_output(
            content,
            timestamp_filename("onboarding_plan", "md"),
            str(get_output_dir("onboarding")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Onboarding Generator - مولّد خطط تهيئة الموظفين"
    )
    parser.add_argument(
        "--role", required=True, help="Job role/title"
    )
    parser.add_argument(
        "--department", default="", help="Department name"
    )
    parser.add_argument(
        "--company-size",
        choices=["small", "medium", "large"],
        default="medium",
        help="Company size",
    )
    parser.add_argument(
        "--week", type=int, default=0,
        help="Generate checklist for specific week (1-12)",
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = OnboardingGenerator()

    if args.week > 0:
        print(gen.generate_checklist(
            args.role, week=args.week, language=args.language,
        ))
    elif args.save:
        path = gen.generate_and_save(
            args.role,
            department=args.department,
            company_size=args.company_size,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(gen.generate(
            args.role,
            department=args.department,
            company_size=args.company_size,
            language=args.language,
        ))


if __name__ == "__main__":
    main()
