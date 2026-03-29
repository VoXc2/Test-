"""AI Tutoring Bot - Income Stream.

Provides personalized tutoring with step-by-step explanations,
practice problems, and adaptive learning. Supports Arabic and English.

Business Model:
- Per-session tutoring: 50-150 SAR
- Monthly subscription: 200-500 SAR/student
- School partnerships: 2000-10000 SAR/month
- Subject-specific packages: 300-800 SAR

Usage:
    python -m income_streams.tutoring_bot.tutor --subject "الرياضيات" --question "اشرح نظرية فيثاغورس"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class TutoringBot:
    """AI-powered personalized tutoring assistant."""

    def __init__(self):
        self.client = AIClient()

    def explain(
        self,
        subject: str,
        question: str,
        level: str = "intermediate",
        language: str = "ar",
    ) -> str:
        """Explain a concept or answer a question with clear, engaging style.

        Args:
            subject: The subject area (e.g., math, science, Arabic)
            question: The specific question or concept to explain
            level: beginner, intermediate, or advanced
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"
        level_map = {
            "beginner": "مبتدئ - استخدم لغة بسيطة جداً وأمثلة من الحياة اليومية",
            "intermediate": "متوسط - استخدم مصطلحات تقنية مع شرحها",
            "advanced": "متقدم - استخدم المصطلحات المتخصصة وتعمق في التفاصيل",
        }
        level_text = level_map.get(level, level_map["intermediate"])

        system = """مدرس خصوصي خبير يشرح بأسلوب مبسط وممتع. يستخدم أمثلة من الحياة اليومية لتقريب المفاهيم.
يتدرج من البسيط للمعقد ويتأكد من فهم الطالب في كل خطوة.

قواعدك:
- ابدأ بربط المفهوم بشيء يعرفه الطالب من حياته اليومية
- قسّم الشرح لخطوات صغيرة ومتدرجة
- استخدم أمثلة متعددة ومتنوعة
- أضف رسوماً توضيحية بالنص (ASCII art) عند الحاجة
- اختبر الفهم بأسئلة بسيطة بعد كل مفهوم
- شجع الطالب واستخدم أسلوباً إيجابياً
- إذا كان المفهوم صعباً، قدم طريقة بديلة للشرح"""

        prompt = f"""اشرح باللغة {lang} بأسلوب مبسط وممتع:

المادة: {subject}
السؤال/المفهوم: {question}
مستوى الطالب: {level_text}

قدم الشرح بالتنسيق التالي:

# {question}

## 🎯 الفكرة الأساسية
(جملة واحدة تلخص المفهوم بأبسط طريقة)

## 📖 الشرح المبسط
(ابدأ بمثال من الحياة اليومية ثم انتقل للمفهوم العلمي)

## 📝 الشرح التفصيلي
(شرح خطوة بخطوة مع أمثلة)

## 💡 أمثلة عملية
(3-5 أمثلة متدرجة في الصعوبة)

## ❓ اختبر فهمك
(3 أسئلة بسيطة للتأكد من الفهم)

## 🔗 مفاهيم مرتبطة
(مواضيع ذات صلة يمكن دراستها لاحقاً)

## 💪 نصيحة للمذاكرة
(كيف يحفظ ويفهم هذا المفهوم)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def solve_step_by_step(
        self,
        problem: str,
        language: str = "ar",
    ) -> str:
        """Solve a problem with detailed step-by-step explanation.

        Args:
            problem: The problem to solve
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """مدرس خصوصي خبير يشرح بأسلوب مبسط وممتع. يستخدم أمثلة من الحياة اليومية.
يتدرج من البسيط للمعقد ويحل المسائل خطوة بخطوة مع توضيح السبب وراء كل خطوة.

قواعدك:
- اكتب المسألة بوضوح أولاً
- حدد المعطيات والمطلوب
- اشرح كل خطوة والسبب وراءها
- تأكد من صحة الحل بالتحقق"""

        prompt = f"""حل المسألة التالية خطوة بخطوة باللغة {lang}:

المسألة: {problem}

قدم الحل بالتنسيق التالي:

# حل المسألة

## المعطيات
(ما هي المعلومات المتاحة)

## المطلوب
(ماذا نريد أن نجد)

## القوانين/القواعد المستخدمة
(ما القوانين التي سنستخدمها)

## خطوات الحل

### الخطوة 1:
(الخطوة + الشرح + لماذا هذه الخطوة)

### الخطوة 2:
(...)

## النتيجة النهائية
(الجواب بشكل واضح)

## التحقق من الحل
(كيف نتأكد أن الحل صحيح)

## مسائل مشابهة للتدريب
(2-3 مسائل مشابهة يمكن حلها)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_practice(
        self,
        topic: str,
        num_problems: int = 5,
        language: str = "ar",
    ) -> str:
        """Generate practice problems on a specific topic.

        Args:
            topic: The topic to generate practice problems for
            num_problems: Number of problems to generate
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """مدرس خصوصي خبير يشرح بأسلوب مبسط وممتع. يستخدم أمثلة من الحياة اليومية.
يتدرج من البسيط للمعقد. يصمم تمارين متدرجة في الصعوبة تغطي جوانب مختلفة من الموضوع."""

        prompt = f"""أنشئ {num_problems} تمارين تدريبية باللغة {lang} عن:

الموضوع: {topic}

# تمارين تدريبية: {topic}

## التمارين
(تمارين متدرجة من السهل للصعب)
لكل تمرين:
- نص التمرين بوضوح
- مستوى الصعوبة (سهل/متوسط/صعب)
- تلميح للحل

## الحلول التفصيلية
(حل كل تمرين خطوة بخطوة)

## نصائح عامة
(نصائح للتعامل مع هذا النوع من المسائل)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        subject: str,
        question: str,
        level: str = "intermediate",
        language: str = "ar",
    ) -> str:
        """Explain a concept and save the explanation to a file."""
        content = self.explain(subject, question, level=level, language=language)
        filename = timestamp_filename("tutoring", "md")
        return save_output(content, filename, str(get_output_dir("tutoring")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Tutoring Bot - Personalized tutoring and explanations"
    )
    parser.add_argument(
        "--subject", required=True, help="Subject area (e.g., 'الرياضيات')"
    )
    parser.add_argument(
        "--question", required=True, help="Question or concept to explain"
    )
    parser.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate",
        help="Student level (default: intermediate)",
    )
    parser.add_argument(
        "--language",
        choices=["ar", "en"],
        default="ar",
        help="Output language (default: ar)",
    )
    parser.add_argument(
        "--solve",
        action="store_true",
        help="Solve step-by-step instead of explaining",
    )
    parser.add_argument(
        "--practice",
        type=int,
        default=0,
        help="Generate N practice problems instead of explaining",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = TutoringBot()

    if args.solve:
        result = gen.solve_step_by_step(args.question, language=args.language)
    elif args.practice > 0:
        result = gen.generate_practice(
            args.question, num_problems=args.practice, language=args.language
        )
    elif args.save:
        result = gen.generate_and_save(
            args.subject,
            args.question,
            level=args.level,
            language=args.language,
        )
        print(f"Saved to: {result}")
        return
    else:
        result = gen.explain(
            args.subject,
            args.question,
            level=args.level,
            language=args.language,
        )

    print(result)


if __name__ == "__main__":
    main()
