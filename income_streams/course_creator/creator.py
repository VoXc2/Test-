"""AI Course Creator - Income Stream.

Generates comprehensive educational courses with structured modules,
lessons, exercises, and assessments. Supports Arabic and English.

Business Model:
- Single course design: 500-2000 SAR
- Course platform setup: 2000-5000 SAR
- Corporate training courses: 3000-10000 SAR
- Monthly retainer: 5000-15000 SAR

Usage:
    python -m income_streams.course_creator.creator --title "Python للمبتدئين"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class CourseCreator:
    """AI-powered educational course creator."""

    def __init__(self):
        self.client = AIClient()

    def generate_course(
        self,
        title: str,
        level: str = "beginner",
        modules: int = 8,
        language: str = "ar",
    ) -> str:
        """Generate a full course structure with modules, lessons, and assessments.

        Args:
            title: Course title / topic
            level: beginner, intermediate, or advanced
            modules: Number of modules in the course
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"
        level_map = {
            "beginner": "مبتدئ",
            "intermediate": "متوسط",
            "advanced": "متقدم",
        }
        level_ar = level_map.get(level, level)

        system = """خبير تصميم تعليمي (Instructional Designer) مع 10 سنوات خبرة في تصميم الدورات التدريبية والمناهج التعليمية.
يصمم دورات تتبع معايير ADDIE (التحليل، التصميم، التطوير، التنفيذ، التقييم) ونموذج Bloom للأهداف التعليمية.
يكتب أهداف تعليمية SMART (محددة، قابلة للقياس، قابلة للتحقيق، ذات صلة، محددة زمنياً).

قواعدك:
- صمم كل وحدة بأهداف تعليمية واضحة ومحددة
- استخدم تصنيف بلوم في صياغة الأهداف (تذكر، فهم، تطبيق، تحليل، تقييم، إبداع)
- أضف تمارين عملية وأنشطة تفاعلية لكل درس
- صمم اختبارات تقيس مستويات مختلفة من الفهم
- اجعل التقدم تدريجياً من البسيط للمعقد
- أضف مشروعاً نهائياً يجمع كل المهارات المكتسبة"""

        prompt = f"""صمم دورة تدريبية كاملة ومفصلة باللغة {lang}:

عنوان الدورة: {title}
المستوى: {level_ar}
عدد الوحدات: {modules}

يجب أن تشمل الدورة:

# عنوان الدورة
## الوصف التعريفي
(فقرة شاملة عن الدورة وفوائدها)

## المتطلبات المسبقة
(قائمة بالمتطلبات اللازمة)

## الأهداف التعليمية العامة
(أهداف SMART للدورة ككل)

## الفئة المستهدفة
(من يستفيد من هذه الدورة)

## الوحدات التعليمية ({modules} وحدات)
لكل وحدة:
### الوحدة X: [العنوان]
- **الأهداف التعليمية**: (3-5 أهداف SMART)
- **الدروس**:
  - الدرس 1: [العنوان] (الوصف + المدة)
  - الدرس 2: ...
- **التمارين العملية**: (2-3 تمارين تطبيقية)
- **اختبار الوحدة**: (وصف الاختبار ومعايير النجاح)

## المشروع النهائي
(وصف تفصيلي للمشروع + معايير التقييم + الجدول الزمني)

## شهادة الإتمام
(متطلبات الحصول على الشهادة + المهارات المكتسبة)

## المدة الإجمالية والجدول المقترح

اجعل المحتوى شاملاً وعملياً وقابلاً للتطبيق مباشرة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_lesson(
        self,
        course_title: str,
        lesson_topic: str,
        language: str = "ar",
    ) -> str:
        """Generate a detailed lesson plan for a specific topic within a course.

        Args:
            course_title: The parent course title
            lesson_topic: The specific lesson topic
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """خبير تصميم تعليمي (Instructional Designer) مع 10 سنوات خبرة في تصميم الدورات التدريبية والمناهج التعليمية.
يصمم دورات تتبع معايير ADDIE ونموذج Bloom للأهداف التعليمية.
يكتب أهداف تعليمية SMART.

قواعدك:
- صمم الدرس بمقدمة وعرض وخاتمة واضحة
- أضف أمثلة عملية من الواقع
- استخدم أنشطة تفاعلية لتثبيت المعلومات
- أضف أسئلة للتقييم الذاتي"""

        prompt = f"""صمم درساً تفصيلياً باللغة {lang}:

الدورة: {course_title}
موضوع الدرس: {lesson_topic}

يجب أن يشمل الدرس:

# عنوان الدرس
## الأهداف التعليمية
(ماذا سيتعلم الطالب بنهاية الدرس)

## المقدمة والتمهيد
(ربط الدرس بما سبق + إثارة الفضول)

## المحتوى التعليمي
(شرح تفصيلي مع أمثلة وتوضيحات)

## الأنشطة التفاعلية
(تمارين أثناء الدرس)

## التمارين العملية
(تطبيقات عملية بعد الدرس)

## ملخص الدرس
(النقاط الرئيسية)

## التقييم الذاتي
(أسئلة لقياس الفهم)

## مصادر إضافية
(مراجع وروابط للاستزادة)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        title: str,
        level: str = "beginner",
        modules: int = 8,
        language: str = "ar",
    ) -> str:
        """Generate a course and save it to a file."""
        content = self.generate_course(
            title, level=level, modules=modules, language=language
        )
        filename = timestamp_filename("course", "md")
        return save_output(content, filename, str(get_output_dir("courses")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Course Creator - Generate comprehensive educational courses"
    )
    parser.add_argument(
        "--title", required=True, help="Course title (e.g., 'Python للمبتدئين')"
    )
    parser.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        default="beginner",
        help="Course difficulty level (default: beginner)",
    )
    parser.add_argument(
        "--modules",
        type=int,
        default=8,
        help="Number of modules in the course (default: 8)",
    )
    parser.add_argument(
        "--language",
        choices=["ar", "en"],
        default="ar",
        help="Output language (default: ar)",
    )
    parser.add_argument(
        "--lesson",
        help="Generate a single lesson on this topic instead of full course",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = CourseCreator()

    if args.lesson:
        result = gen.generate_lesson(args.title, args.lesson, language=args.language)
    elif args.save:
        result = gen.generate_and_save(
            args.title,
            level=args.level,
            modules=args.modules,
            language=args.language,
        )
        print(f"Saved to: {result}")
        return
    else:
        result = gen.generate_course(
            args.title,
            level=args.level,
            modules=args.modules,
            language=args.language,
        )

    print(result)


if __name__ == "__main__":
    main()
