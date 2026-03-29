"""AI Training Program Builder - Income Stream.

Generates corporate training programs, workshops, and assessments
following CIPD and ATD standards. Supports Arabic and English.

Business Model:
- Training program design: 2000-8000 SAR
- Workshop facilitation guide: 1000-3000 SAR
- Full training package: 5000-20000 SAR
- Annual corporate contract: 20000-100000 SAR

Usage:
    python -m income_streams.training_programs.program_builder --company "شركة أرامكو" --topic "القيادة"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class TrainingProgramBuilder:
    """AI-powered corporate training program designer."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        company: str,
        topic: str,
        duration: str = "3 days",
        audience: str = "employees",
        language: str = "ar",
    ) -> str:
        """Generate a comprehensive corporate training program.

        Args:
            company: Company name for customization
            topic: Training topic
            duration: Program duration (e.g., '3 days', '1 week')
            audience: Target audience (employees, managers, executives)
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"
        audience_map = {
            "employees": "الموظفين",
            "managers": "المدراء والمشرفين",
            "executives": "القيادات التنفيذية",
            "new_hires": "الموظفين الجدد",
        }
        audience_ar = audience_map.get(audience, audience)

        system = """مستشار تدريب مؤسسي خبير في تطوير الموارد البشرية مع خبرة تزيد عن 15 سنة.
يصمم برامج تدريبية تتبع معايير CIPD (المعهد المعتمد لشؤون الأفراد والتطوير) و ATD (جمعية تطوير المواهب).

قواعدك:
- صمم برامج تحقق أهداف العمل وتطور الكفاءات
- استخدم نموذج كيركباتريك لتقييم التدريب (ردة الفعل، التعلم، السلوك، النتائج)
- أضف أنشطة تفاعلية متنوعة (ورش عمل، دراسات حالة، تمثيل أدوار، مناقشات)
- صمم مواد تدريبية شاملة (عروض تقديمية، أوراق عمل، أدلة المتدرب)
- اربط البرنامج بمؤشرات أداء قابلة للقياس KPIs
- خصص المحتوى حسب طبيعة الشركة والجمهور المستهدف"""

        prompt = f"""صمم برنامجاً تدريبياً شاملاً باللغة {lang}:

الشركة: {company}
الموضوع: {topic}
المدة: {duration}
الفئة المستهدفة: {audience_ar}

يجب أن يشمل البرنامج:

# برنامج تدريبي: {topic}
## لشركة {company}

### نبذة عن البرنامج
(وصف شامل وأهمية البرنامج)

### الأهداف العامة
(أهداف SMART للبرنامج)

### الأهداف التفصيلية
(ماذا سيتمكن المتدرب من فعله بعد البرنامج)

### الفئة المستهدفة والمتطلبات
(من يحضر + المتطلبات المسبقة)

### الجدول التفصيلي
لكل يوم:
#### اليوم X: [العنوان]
| الوقت | النشاط | الوصف | الأسلوب |
|-------|--------|-------|---------|
| 9:00-9:30 | الافتتاح | ... | عرض تقديمي |
| 9:30-10:30 | الجلسة 1 | ... | ورشة عمل |
| ... | ... | ... | ... |

### المواد التدريبية
(قائمة بجميع المواد المطلوبة)
- عروض تقديمية
- أوراق عمل
- دراسات حالة
- أدلة المتدرب/المدرب

### الأنشطة التفاعلية
(وصف تفصيلي لكل نشاط)
- ورش العمل
- دراسات الحالة
- تمثيل الأدوار
- المناقشات الجماعية
- الألعاب التدريبية

### التقييم (نموذج كيركباتريك)
- المستوى 1 - ردة الفعل: (استبيان رضا المتدربين)
- المستوى 2 - التعلم: (اختبار قبلي وبعدي)
- المستوى 3 - السلوك: (خطة متابعة بعد التدريب)
- المستوى 4 - النتائج: (مؤشرات الأداء KPIs)

### الشهادات
(شهادة إتمام + المعايير المطلوبة)

### الميزانية التقديرية
(تكاليف المواد والمكان والمدرب)

### خطة المتابعة
(أنشطة ما بعد التدريب لضمان نقل أثر التعلم)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_workshop(
        self,
        topic: str,
        hours: int = 4,
        language: str = "ar",
    ) -> str:
        """Generate a focused workshop plan.

        Args:
            topic: Workshop topic
            hours: Workshop duration in hours
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """مستشار تدريب مؤسسي خبير في تطوير الموارد البشرية.
يصمم برامج تدريبية تتبع معايير CIPD و ATD.
يصمم ورش عمل تفاعلية تركز على التطبيق العملي والمشاركة الفعالة."""

        prompt = f"""صمم ورشة عمل تفاعلية باللغة {lang}:

الموضوع: {topic}
المدة: {hours} ساعات

# ورشة عمل: {topic}

## الهدف العام
(هدف واحد واضح للورشة)

## الأهداف التفصيلية
(3-5 أهداف محددة)

## المتطلبات
- متطلبات المكان والتجهيزات
- المواد المطلوبة
- عدد المشاركين المثالي

## الجدول الزمني
| الوقت | النشاط | الوصف | المدة |
|-------|--------|-------|-------|
| ... | ... | ... | ... |

## الأنشطة التفاعلية
لكل نشاط:
- الاسم والهدف
- التعليمات خطوة بخطوة
- المواد المطلوبة
- وقت المناقشة

## أوراق العمل
(محتوى أوراق العمل للمشاركين)

## التقييم
(كيف نقيس نجاح الورشة)

## ملاحظات للميسّر
(نصائح لتقديم الورشة بنجاح)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_assessment(
        self,
        program_topic: str,
        language: str = "ar",
    ) -> str:
        """Generate training assessment tools for a program.

        Args:
            program_topic: The training program topic to assess
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """مستشار تدريب مؤسسي خبير في تطوير الموارد البشرية.
يصمم برامج تدريبية تتبع معايير CIPD و ATD.
يصمم أدوات تقييم شاملة تقيس أثر التدريب على مختلف المستويات."""

        prompt = f"""صمم أدوات تقييم شاملة باللغة {lang} لبرنامج تدريبي عن:

الموضوع: {program_topic}

# أدوات تقييم البرنامج التدريبي: {program_topic}

## 1. الاختبار القبلي
(10 أسئلة لقياس المستوى قبل التدريب)

## 2. الاختبار البعدي
(10 أسئلة لقياس المستوى بعد التدريب)

## 3. استبيان رضا المتدربين
(استبيان شامل عن جودة التدريب)

## 4. نموذج تقييم المدرب
(معايير تقييم أداء المدرب)

## 5. خطة المتابعة
(نموذج متابعة تطبيق المهارات بعد 30/60/90 يوم)

## 6. مؤشرات الأداء KPIs
(مؤشرات قابلة للقياس لنجاح البرنامج)

## 7. تقرير ROI التدريب
(نموذج حساب العائد على الاستثمار في التدريب)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        company: str,
        topic: str,
        duration: str = "3 days",
        audience: str = "employees",
        language: str = "ar",
    ) -> str:
        """Generate a training program and save it to a file."""
        content = self.generate(
            company,
            topic,
            duration=duration,
            audience=audience,
            language=language,
        )
        filename = timestamp_filename("training_program", "md")
        return save_output(content, filename, str(get_output_dir("training")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Training Program Builder - Design corporate training programs"
    )
    parser.add_argument(
        "--company", required=True, help="Company name (e.g., 'شركة أرامكو')"
    )
    parser.add_argument(
        "--topic", required=True, help="Training topic (e.g., 'القيادة')"
    )
    parser.add_argument(
        "--duration",
        default="3 days",
        help="Program duration (default: '3 days')",
    )
    parser.add_argument(
        "--audience",
        choices=["employees", "managers", "executives", "new_hires"],
        default="employees",
        help="Target audience (default: employees)",
    )
    parser.add_argument(
        "--language",
        choices=["ar", "en"],
        default="ar",
        help="Output language (default: ar)",
    )
    parser.add_argument(
        "--workshop",
        type=int,
        default=0,
        help="Generate a workshop of N hours instead of full program",
    )
    parser.add_argument(
        "--assessment",
        action="store_true",
        help="Generate assessment tools instead of full program",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = TrainingProgramBuilder()

    if args.workshop > 0:
        result = gen.generate_workshop(
            args.topic, hours=args.workshop, language=args.language
        )
    elif args.assessment:
        result = gen.generate_assessment(args.topic, language=args.language)
    elif args.save:
        result = gen.generate_and_save(
            args.company,
            args.topic,
            duration=args.duration,
            audience=args.audience,
            language=args.language,
        )
        print(f"Saved to: {result}")
        return
    else:
        result = gen.generate(
            args.company,
            args.topic,
            duration=args.duration,
            audience=args.audience,
            language=args.language,
        )

    print(result)


if __name__ == "__main__":
    main()
