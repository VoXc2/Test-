"""AI Job Description Generator - Income Stream.

Generates professional job descriptions optimized for attracting
top candidates and compliant with Saudi labor regulations.

Business Model:
- Single job description: 50-150 SAR
- Bulk package (10+): 300-800 SAR
- Monthly subscription for HR teams: 200-500 SAR

Usage:
    python -m income_streams.job_descriptions.generator --title "مهندس برمجيات" --seniority senior
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


SENIORITY_MAP = {
    "junior": "مبتدئ",
    "mid": "متوسط الخبرة",
    "senior": "خبير",
    "lead": "قائد فريق",
    "executive": "تنفيذي",
}

PLATFORM_MAP = {
    "linkedin": "LinkedIn",
    "bayt": "Bayt.com",
    "indeed": "Indeed",
    "twitter": "Twitter/X",
}


class JobDescriptionGenerator:
    """AI-powered job description generator for Saudi/Gulf market."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        title: str,
        company: str = "",
        seniority: str = "mid",
        industry: str = "",
        language: str = "ar",
    ) -> str:
        """Generate a professional job description.

        Args:
            title: Job title
            company: Company name (optional)
            seniority: junior, mid, senior, lead, or executive
            industry: Industry/sector
            language: 'ar' or 'en'
        """
        seniority_ar = SENIORITY_MAP.get(seniority, seniority)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير توظيف ومستشار موارد بشرية متخصص في السوق السعودي والخليجي. "
            "يكتب أوصاف وظيفية تجذب أفضل المرشحين وتتوافق مع نظام العمل السعودي. "
            "يراعي متطلبات السعودة ونطاقات وبرنامج نطاقات المطور. "
            "يستخدم لغة شاملة وجاذبة تعكس ثقافة الشركة. "
            "يضمن وضوح المتطلبات والمسؤوليات لجذب المرشحين المناسبين."
        )

        company_text = f"\nالشركة: {company}" if company else ""
        industry_text = f"\nالقطاع: {industry}" if industry else ""

        prompt = (
            f"اكتب وصف وظيفي احترافي وشامل {lang}.\n\n"
            f"المسمى الوظيفي: {title}\n"
            f"مستوى الأقدمية: {seniority_ar}\n"
            f"{company_text}{industry_text}\n\n"
            "اكتب الأقسام التالية:\n"
            "1. المسمى الوظيفي الرسمي\n"
            "2. عن الشركة (فقرة جاذبة)\n"
            "3. الوصف العام للدور (فقرة)\n"
            "4. المسؤوليات والمهام الرئيسية (10+ نقاط)\n"
            "5. المؤهلات المطلوبة (must-have)\n"
            "6. المؤهلات المفضلة (nice-to-have)\n"
            "7. المهارات التقنية والشخصية\n"
            "8. سنوات الخبرة المطلوبة\n"
            "9. المزايا والتعويضات\n"
            "10. طريقة التقديم\n\n"
            "اجعل الوصف جاذباً ومهنياً ومتوافقاً مع نظام العمل السعودي."
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_for_platform(
        self,
        title: str,
        platform: str = "linkedin",
        language: str = "ar",
    ) -> str:
        """Generate a job description optimized for a specific platform.

        Args:
            title: Job title
            platform: linkedin, bayt, indeed, or twitter
            language: 'ar' or 'en'
        """
        platform_name = PLATFORM_MAP.get(platform, platform)
        lang = "بالعربية" if language == "ar" else "in English"

        system = (
            "خبير توظيف متخصص في كتابة إعلانات الوظائف لمنصات التوظيف المختلفة. "
            "يعرف أفضل الممارسات لكل منصة لتحقيق أعلى وصول وتفاعل."
        )

        prompt = (
            f"اكتب إعلان وظيفي {lang} مُحسّن لمنصة {platform_name}.\n\n"
            f"المسمى: {title}\n\n"
            f"راعِ خصائص منصة {platform_name}:\n"
            "- الطول المناسب للمنصة\n"
            "- الكلمات المفتاحية للبحث\n"
            "- التنسيق الأمثل\n"
            "- الهاشتاقات المناسبة (إن وجدت)\n"
            "- دعوة واضحة للتقديم (CTA)"
        )

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)

    def generate_and_save(
        self,
        title: str,
        company: str = "",
        seniority: str = "mid",
        industry: str = "",
        language: str = "ar",
    ) -> str:
        """Generate a job description and save it to file."""
        content = self.generate(
            title, company=company, seniority=seniority,
            industry=industry, language=language,
        )
        return save_output(
            content,
            timestamp_filename("job_description", "md"),
            str(get_output_dir("job_descriptions")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="AI Job Description Generator - مولّد الأوصاف الوظيفية"
    )
    parser.add_argument(
        "--title", required=True, help="Job title"
    )
    parser.add_argument(
        "--company", default="", help="Company name"
    )
    parser.add_argument(
        "--seniority",
        choices=["junior", "mid", "senior", "lead", "executive"],
        default="mid",
        help="Seniority level",
    )
    parser.add_argument(
        "--industry", default="", help="Industry/sector"
    )
    parser.add_argument(
        "--platform", default="",
        choices=["", "linkedin", "bayt", "indeed", "twitter"],
        help="Optimize for platform",
    )
    parser.add_argument(
        "--language", default="ar", choices=["ar", "en"], help="Output language"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = JobDescriptionGenerator()

    if args.platform:
        print(gen.generate_for_platform(
            args.title, platform=args.platform, language=args.language,
        ))
    elif args.save:
        path = gen.generate_and_save(
            args.title,
            company=args.company,
            seniority=args.seniority,
            industry=args.industry,
            language=args.language,
        )
        print(f"Saved to: {path}")
    else:
        print(gen.generate(
            args.title,
            company=args.company,
            seniority=args.seniority,
            industry=args.industry,
            language=args.language,
        ))


if __name__ == "__main__":
    main()
