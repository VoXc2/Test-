"""AI Quiz Generator - Income Stream.

Generates educational quizzes and assessments with multiple question types,
answer keys, and grading rubrics. Supports Arabic and English.

Business Model:
- Quiz bank per subject: 200-500 SAR
- Full exam preparation: 500-1500 SAR
- School/institution contracts: 2000-8000 SAR/month
- Platform integration: 5000-15000 SAR

Usage:
    python -m income_streams.quiz_generator.generator --subject "الرياضيات" --grade "الصف السادس"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class QuizGenerator:
    """AI-powered educational quiz and assessment generator."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        subject: str,
        grade: str = "",
        num_questions: int = 20,
        question_types: str = "mixed",
        language: str = "ar",
    ) -> str:
        """Generate a comprehensive quiz/assessment.

        Args:
            subject: Subject or topic for the quiz
            grade: Grade level or target audience
            num_questions: Number of questions to generate
            question_types: mixed, mcq, essay, true_false
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"
        grade_text = f"للمرحلة/الصف: {grade}" if grade else ""

        types_map = {
            "mixed": "مزيج من اختيار متعدد + صح/خطأ + أكمل الفراغ + أسئلة مقالية",
            "mcq": "اختيار من متعدد فقط (4 خيارات لكل سؤال)",
            "essay": "أسئلة مقالية وتحليلية فقط",
            "true_false": "أسئلة صح وخطأ فقط",
        }
        types_text = types_map.get(question_types, types_map["mixed"])

        system = """معلم خبير في التقييم التعليمي مع خبرة واسعة في تصميم الاختبارات والتقييمات.
يصمم اختبارات تقيس مستويات التفكير المختلفة حسب تصنيف بلوم (تذكر، فهم، تطبيق، تحليل، تقييم، إبداع).

قواعدك:
- صمم أسئلة واضحة ومحددة بدون غموض
- وزع الأسئلة على مستويات بلوم المختلفة
- اجعل خيارات الاختيار المتعدد متقاربة ومنطقية (بدون خيارات سخيفة)
- أضف أسئلة تقيس الفهم العميق وليس الحفظ فقط
- صمم نموذج إجابة واضح مع توزيع الدرجات
- أضف معايير تقييم للأسئلة المقالية"""

        prompt = f"""صمم اختباراً شاملاً باللغة {lang}:

المادة/الموضوع: {subject}
{grade_text}
عدد الأسئلة: {num_questions}
نوع الأسئلة: {types_text}

يجب أن يشمل الاختبار:

# عنوان الاختبار
## معلومات الاختبار
- المادة: {subject}
- المدة الزمنية: (حدد المدة المناسبة)
- الدرجة الكلية: (حدد الدرجة)
- تاريخ الاختبار: ___

## التعليمات العامة
(تعليمات واضحة للطالب)

## القسم الأول: أسئلة اختيار من متعدد
(أسئلة مع 4 خيارات لكل سؤال)

## القسم الثاني: أسئلة صح وخطأ
(مع تصحيح العبارات الخاطئة)

## القسم الثالث: أكمل الفراغ
(جمل ناقصة تحتاج إكمال)

## القسم الرابع: أسئلة مقالية
(أسئلة تحليلية ونقدية)

---

## نموذج الإجابة
(إجابات جميع الأسئلة مع التوضيح)

## معايير التقييم
(توزيع الدرجات + معايير تقييم الأسئلة المقالية)

## جدول المواصفات
(ربط الأسئلة بمستويات بلوم)

اجعل الأسئلة متنوعة المستوى ومناسبة للفئة المستهدفة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_answer_key(self, quiz_text: str, language: str = "ar") -> str:
        """Generate a detailed answer key for an existing quiz.

        Args:
            quiz_text: The quiz text to generate answers for
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """معلم خبير في التقييم التعليمي. يصمم نماذج إجابة تفصيلية مع شرح وافٍ لكل إجابة.
يوضح خطوات الحل ومعايير التقييم بدقة."""

        prompt = f"""أنشئ نموذج إجابة تفصيلي باللغة {lang} للاختبار التالي:

{quiz_text}

يجب أن يشمل نموذج الإجابة:

# نموذج الإجابة التفصيلي

## الإجابات مع الشرح
لكل سؤال:
- الإجابة الصحيحة
- شرح مفصل لسبب صحة الإجابة
- الأخطاء الشائعة المتوقعة

## توزيع الدرجات
(درجة كل سؤال + معايير الدرجات الجزئية)

## ملاحظات للمصحح
(إرشادات التصحيح + حالات خاصة)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        subject: str,
        grade: str = "",
        num_questions: int = 20,
        question_types: str = "mixed",
        language: str = "ar",
    ) -> str:
        """Generate a quiz and save it to a file."""
        content = self.generate(
            subject,
            grade=grade,
            num_questions=num_questions,
            question_types=question_types,
            language=language,
        )
        filename = timestamp_filename("quiz", "md")
        return save_output(content, filename, str(get_output_dir("quizzes")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Quiz Generator - Generate educational quizzes and assessments"
    )
    parser.add_argument(
        "--subject", required=True, help="Subject or topic (e.g., 'الرياضيات')"
    )
    parser.add_argument(
        "--grade", default="", help="Grade level (e.g., 'الصف السادس')"
    )
    parser.add_argument(
        "--questions",
        type=int,
        default=20,
        help="Number of questions (default: 20)",
    )
    parser.add_argument(
        "--types",
        choices=["mixed", "mcq", "essay", "true_false"],
        default="mixed",
        help="Question types (default: mixed)",
    )
    parser.add_argument(
        "--language",
        choices=["ar", "en"],
        default="ar",
        help="Output language (default: ar)",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = QuizGenerator()

    if args.save:
        result = gen.generate_and_save(
            args.subject,
            grade=args.grade,
            num_questions=args.questions,
            question_types=args.types,
            language=args.language,
        )
        print(f"Saved to: {result}")
    else:
        result = gen.generate(
            args.subject,
            grade=args.grade,
            num_questions=args.questions,
            question_types=args.types,
            language=args.language,
        )
        print(result)


if __name__ == "__main__":
    main()
