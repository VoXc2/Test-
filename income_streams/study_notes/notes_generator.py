"""AI Study Notes Generator - Income Stream.

Transforms content into structured study notes, flashcards, mind maps,
and Cornell notes. Supports Arabic and English.

Business Model:
- Study notes package: 100-300 SAR
- Full subject preparation: 500-1500 SAR
- Student subscriptions: 50-150 SAR/month
- University bulk deals: 3000-10000 SAR/semester

Usage:
    python -m income_streams.study_notes.notes_generator --content "..." --format summary
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class StudyNotesGenerator:
    """AI-powered study notes and learning materials generator."""

    def __init__(self):
        self.client = AIClient()

    def generate_notes(
        self,
        content: str,
        format: str = "summary",
        subject: str = "",
        language: str = "ar",
    ) -> str:
        """Generate study notes from content in various formats.

        Args:
            content: The source content to transform into notes
            format: summary, flashcards, mind_map, or cornell_notes
            subject: Subject area for context
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"
        subject_text = f"المادة: {subject}" if subject else ""

        system = """خبير تلخيص أكاديمي يحول المحتوى الطويل لملاحظات مركزة وفعالة.
يستخدم تقنيات Cornell Notes و Feynman Technique لتبسيط المفاهيم المعقدة.

قواعدك:
- استخرج الأفكار الرئيسية والنقاط المهمة
- نظم المعلومات بتسلسل منطقي
- استخدم العناوين والنقاط لسهولة المراجعة
- أضف كلمات مفتاحية وتعريفات مهمة
- ربط المفاهيم ببعضها البعض
- أضف أمثلة توضيحية مختصرة
- استخدم تقنية Feynman: اشرح كأنك تعلم شخصاً مبتدئاً"""

        format_instructions = {
            "summary": f"""حول المحتوى التالي إلى ملخص دراسي مركز باللغة {lang}:

{subject_text}
المحتوى: {content}

# ملخص دراسي

## النقاط الرئيسية
(أهم الأفكار في نقاط مرقمة)

## المفاهيم الأساسية
(تعريف كل مفهوم بجملة واحدة)

## الشرح المبسط
(شرح بأسلوب Feynman - كأنك تشرح لمبتدئ)

## الروابط والعلاقات
(كيف ترتبط المفاهيم ببعضها)

## أسئلة للمراجعة
(5 أسئلة تغطي أهم النقاط)

## ملخص سريع
(فقرة واحدة تلخص كل شيء)""",

            "flashcards": f"""حول المحتوى التالي إلى بطاقات تعليمية (Flashcards) باللغة {lang}:

{subject_text}
المحتوى: {content}

# بطاقات تعليمية

أنشئ 20 بطاقة تعليمية بالتنسيق:

## البطاقة 1
**السؤال (الوجه الأمامي):** ...
**الجواب (الوجه الخلفي):** ...
**الفئة:** (مفهوم/تعريف/قاعدة/مثال)
**مستوى الصعوبة:** (سهل/متوسط/صعب)

(كرر لكل بطاقة)

## نصائح للمراجعة
(كيف تستخدم البطاقات بفعالية - تقنية Spaced Repetition)""",

            "mind_map": f"""حول المحتوى التالي إلى خريطة ذهنية نصية باللغة {lang}:

{subject_text}
المحتوى: {content}

# خريطة ذهنية

## المفهوم المركزي
[العنوان الرئيسي]

### الفرع 1: [العنوان]
  - النقطة 1.1
    - التفصيل 1.1.1
    - التفصيل 1.1.2
  - النقطة 1.2

### الفرع 2: [العنوان]
  - النقطة 2.1
  - النقطة 2.2

(أكمل جميع الفروع)

## الروابط بين الفروع
(كيف ترتبط الفروع ببعضها)

## ملاحظات إضافية
(نقاط مهمة لا تنسَها)""",

            "cornell_notes": f"""حول المحتوى التالي إلى ملاحظات كورنيل (Cornell Notes) باللغة {lang}:

{subject_text}
المحتوى: {content}

# ملاحظات كورنيل

## معلومات الموضوع
- الموضوع: ...
- التاريخ: ...
- المادة: {subject if subject else "..."}

| الأسئلة/الكلمات المفتاحية | الملاحظات الرئيسية |
|---|---|
| (سؤال أو كلمة مفتاحية) | (الملاحظات التفصيلية) |
| ... | ... |

## الملخص
(3-5 جمل تلخص أهم النقاط - اكتبها بأسلوبك الخاص)

## أسئلة للمراجعة
(أسئلة مهمة للاختبار)

## خطة المراجعة
(متى وكيف تراجع هذه الملاحظات)""",
        }

        prompt = format_instructions.get(format, format_instructions["summary"])
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_flashcards(
        self,
        content: str,
        num_cards: int = 20,
        language: str = "ar",
    ) -> str:
        """Generate flashcards from content.

        Args:
            content: Source content to create flashcards from
            num_cards: Number of flashcards to generate
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """خبير تلخيص أكاديمي يحول المحتوى الطويل لملاحظات مركزة.
يستخدم تقنيات Cornell Notes و Feynman Technique. يصمم بطاقات تعليمية فعالة تركز على المفاهيم الأساسية."""

        prompt = f"""أنشئ {num_cards} بطاقة تعليمية (Flashcards) باللغة {lang} من المحتوى التالي:

{content}

# بطاقات تعليمية ({num_cards} بطاقة)

لكل بطاقة:
## البطاقة [رقم]
**السؤال:** ...
**الجواب:** ...
**ملاحظة:** (نصيحة للتذكر)

## نصائح استخدام البطاقات
- استخدم تقنية التكرار المتباعد (Spaced Repetition)
- راجع البطاقات الصعبة أكثر
- حاول الإجابة قبل قلب البطاقة"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_mind_map(
        self,
        topic: str,
        language: str = "ar",
    ) -> str:
        """Generate a text-based mind map for a topic.

        Args:
            topic: The topic to create a mind map for
            language: 'ar' or 'en'
        """
        lang = "العربية" if language == "ar" else "English"

        system = """خبير تلخيص أكاديمي يحول المحتوى الطويل لملاحظات مركزة.
يستخدم تقنيات Cornell Notes و Feynman Technique. يصمم خرائط ذهنية شاملة تربط المفاهيم ببعضها."""

        prompt = f"""أنشئ خريطة ذهنية شاملة باللغة {lang} عن:

الموضوع: {topic}

# خريطة ذهنية: {topic}

## المفهوم المركزي
🎯 {topic}

### الفرع الرئيسي 1: [العنوان]
  ├── النقطة 1.1
  │   ├── التفصيل أ
  │   └── التفصيل ب
  ├── النقطة 1.2
  └── النقطة 1.3

### الفرع الرئيسي 2: [العنوان]
  ├── النقطة 2.1
  └── النقطة 2.2

(أكمل 4-6 فروع رئيسية مع تفرعاتها)

## الروابط المهمة
(كيف ترتبط الفروع ببعضها - خطوط وصل)

## ملخص الخريطة
(فقرة تربط كل العناصر معاً)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        content: str,
        format: str = "summary",
        subject: str = "",
        language: str = "ar",
    ) -> str:
        """Generate study notes and save to a file."""
        result = self.generate_notes(
            content, format=format, subject=subject, language=language
        )
        filename = timestamp_filename("study_notes", "md")
        return save_output(result, filename, str(get_output_dir("study_notes")))


def main():
    parser = argparse.ArgumentParser(
        description="AI Study Notes Generator - Transform content into study materials"
    )
    parser.add_argument(
        "--content",
        required=True,
        help="Source content to transform into notes",
    )
    parser.add_argument(
        "--format",
        choices=["summary", "flashcards", "mind_map", "cornell"],
        default="summary",
        help="Output format (default: summary)",
    )
    parser.add_argument(
        "--subject", default="", help="Subject area for context"
    )
    parser.add_argument(
        "--language",
        choices=["ar", "en"],
        default="ar",
        help="Output language (default: ar)",
    )
    parser.add_argument(
        "--cards",
        type=int,
        default=20,
        help="Number of flashcards when using --format flashcards (default: 20)",
    )
    parser.add_argument(
        "--save", action="store_true", help="Save output to file"
    )

    args = parser.parse_args()
    gen = StudyNotesGenerator()

    # Map 'cornell' to 'cornell_notes' for internal use
    fmt = "cornell_notes" if args.format == "cornell" else args.format

    if args.format == "flashcards" and args.cards != 20:
        result = gen.generate_flashcards(
            args.content, num_cards=args.cards, language=args.language
        )
    elif args.save:
        result = gen.generate_and_save(
            args.content,
            format=fmt,
            subject=args.subject,
            language=args.language,
        )
        print(f"Saved to: {result}")
        return
    else:
        result = gen.generate_notes(
            args.content,
            format=fmt,
            subject=args.subject,
            language=args.language,
        )

    print(result)


if __name__ == "__main__":
    main()
