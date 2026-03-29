"""AI Resume/CV Builder - Income Stream.

Generates professional CVs and cover letters optimized for ATS systems.
Supports Arabic and English. Huge demand in Saudi market.

Business Model:
- Basic CV: 50-150 SAR
- CV + Cover Letter + LinkedIn: 200-500 SAR
- Executive Package: 500-1500 SAR
- Bulk (universities/organizations): negotiable

Usage:
    python -m income_streams.cv_builder.cv_generator --name "Ahmed" --title "Software Engineer"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.utils import save_output, timestamp_filename
from income_streams.common.config_loader import get_output_dir


class CVGenerator:
    """AI-powered CV/Resume generator."""

    def __init__(self):
        self.client = AIClient()

    def generate_cv(
        self,
        name: str,
        title: str,
        experience: str = "",
        education: str = "",
        skills: str = "",
        language: str = "ar",
        style: str = "professional",
    ) -> str:
        """Generate a professional CV.

        Args:
            name: Full name
            title: Job title / target position
            experience: Work experience description
            education: Education background
            skills: Key skills
            language: 'ar' or 'en'
            style: professional, creative, academic, executive
        """
        lang = "Arabic" if language == "ar" else "English"

        system = f"""أنت خبير كتابة سير ذاتية معتمد (CPRW) متخصص في السوق {'السعودي والخليجي' if language == 'ar' else 'الدولي'}.
تكتب سير ذاتية تتجاوز أنظمة ATS وتجذب مسؤولي التوظيف.

قواعدك:
- استخدم أفعال عمل قوية (قاد، طور، حقق، نفّذ)
- أضف أرقام وإنجازات قابلة للقياس
- اجعل كل نقطة تبدأ بفعل عمل
- رتب المعلومات من الأحدث للأقدم
- استخدم كلمات مفتاحية تتوافق مع ATS
- الأسلوب: {style}
- اللغة: {lang}"""

        prompt = f"""أنشئ سيرة ذاتية احترافية:

الاسم: {name}
المسمى الوظيفي / الهدف: {title}
الخبرات: {experience or 'خبرة متنوعة في المجال'}
التعليم: {education or 'بكالوريوس'}
المهارات: {skills or 'مهارات متنوعة'}

أريد CV بصيغة Markdown يشمل:
1. معلومات التواصل (اسم، إيميل، هاتف، لينكدإن)
2. ملخص مهني (3-4 أسطر قوية)
3. الخبرات العملية (مع إنجازات بأرقام)
4. التعليم
5. المهارات (تقنية + شخصية)
6. الشهادات (إن وجدت)
7. المشاريع المميزة (إن وجدت)

ملاحظة: أضف محتوى واقعي ومتسق حتى لو المعلومات المقدمة محدودة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_cover_letter(
        self,
        name: str,
        target_company: str,
        target_position: str,
        why_interested: str = "",
        language: str = "ar",
    ) -> str:
        """Generate a tailored cover letter."""
        lang = "Arabic" if language == "ar" else "English"

        system = f"أنت خبير كتابة خطابات تقديم. اكتب خطاب جذاب ومخصص بـ{lang}."

        prompt = f"""اكتب خطاب تقديم (Cover Letter):

الاسم: {name}
الشركة المستهدفة: {target_company}
الوظيفة المستهدفة: {target_position}
سبب الاهتمام: {why_interested or 'شغف بالمجال'}

الخطاب يجب أن:
- يكون مخصص للشركة والوظيفة
- يبرز القيمة التي سأضيفها
- يكون 3-4 فقرات
- ينتهي بدعوة للعمل (CTA)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=1500)

    def optimize_linkedin(self, current_profile: str, target_role: str, language: str = "ar") -> str:
        """Optimize LinkedIn profile for better visibility."""
        lang = "Arabic" if language == "ar" else "English"

        system = f"أنت خبير LinkedIn يحسّن البروفايلات لتظهر في نتائج البحث. اكتب بـ{lang}."

        prompt = f"""حسّن بروفايل LinkedIn التالي:

البروفايل الحالي: {current_profile}
الهدف الوظيفي: {target_role}

أعطني:
1. عنوان احترافي جذاب (Headline)
2. ملخص مُحسّن (About) - 300 كلمة
3. كلمات مفتاحية يجب إضافتها
4. نصائح لتحسين الظهور في البحث
5. اقتراحات محتوى للنشر"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_full_package(self, **kwargs) -> dict:
        """Generate CV + Cover Letter + LinkedIn optimization."""
        results = {}

        print("1/3 إنشاء السيرة الذاتية...")
        results["cv"] = self.generate_cv(**{k: v for k, v in kwargs.items()
                                            if k in ("name", "title", "experience", "education", "skills", "language", "style")})

        print("2/3 إنشاء خطاب التقديم...")
        results["cover_letter"] = self.generate_cover_letter(
            name=kwargs.get("name", ""),
            target_company=kwargs.get("target_company", "شركة رائدة"),
            target_position=kwargs.get("title", ""),
            language=kwargs.get("language", "ar"),
        )

        print("3/3 تحسين LinkedIn...")
        results["linkedin"] = self.optimize_linkedin(
            current_profile=f"{kwargs.get('name', '')} - {kwargs.get('title', '')}",
            target_role=kwargs.get("title", ""),
            language=kwargs.get("language", "ar"),
        )

        # Save all files
        output_dir = get_output_dir("reports")
        name = kwargs.get("name", "cv")
        for key, content in results.items():
            filename = timestamp_filename(f"{name}_{key}", "md")
            path = save_output(content, filename, str(output_dir))
            print(f"  Saved: {path}")

        return results


def main():
    parser = argparse.ArgumentParser(description="AI CV Builder - بناء سيرة ذاتية ذكية")
    parser.add_argument("--name", "-n", required=True, help="Full name")
    parser.add_argument("--title", "-t", required=True, help="Target job title")
    parser.add_argument("--experience", "-e", default="", help="Experience summary")
    parser.add_argument("--education", default="", help="Education")
    parser.add_argument("--skills", "-s", default="", help="Skills (comma-separated)")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--full-package", action="store_true", help="Generate CV + Cover Letter + LinkedIn")

    args = parser.parse_args()
    gen = CVGenerator()

    if args.full_package:
        gen.generate_full_package(
            name=args.name, title=args.title, experience=args.experience,
            education=args.education, skills=args.skills, language=args.language,
        )
    else:
        result = gen.generate_cv(
            args.name, args.title, args.experience,
            args.education, args.skills, args.language,
        )
        print(result)


if __name__ == "__main__":
    main()
