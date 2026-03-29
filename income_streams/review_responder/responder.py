"""AI-powered review responder for digital reputation management."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class ReviewResponder:
    """Respond to customer reviews professionally to build reputation and loyalty."""

    def __init__(self):
        self.client = AIClient()

    def respond(
        self,
        review_text: str,
        rating: int,
        business_name: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a professional response to a customer review.

        Args:
            review_text: The customer review text.
            rating: Rating given (1-5).
            business_name: Name of the business.
            language: Output language (default Arabic).

        Returns:
            Professional response to the review.
        """
        system = (
            "خبير إدارة سمعة رقمية ومتخصص في خدمة العملاء. "
            "يرد على التقييمات بطريقة تحول العملاء الغاضبين لمعجبين "
            "وتشجع العملاء الراضين على العودة. "
            "يقدم: رد مخصص للتقييم، نبرة مناسبة (إيجابي/سلبي/محايد)، "
            "حل للمشكلة إن وجدت، دعوة للعودة."
        )
        tone = "إيجابي" if rating >= 4 else ("سلبي" if rating <= 2 else "محايد")
        business_section = f"\nاسم المنشأة: {business_name}" if business_name else ""
        prompt = (
            f"اكتب رداً احترافياً على التقييم التالي:\n\n"
            f"التقييم: {review_text}\n"
            f"النجوم: {rating}/5\n"
            f"النبرة: {tone}{business_section}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن يشمل الرد:\n"
            f"- شكر العميل على وقته\n"
            f"- التعامل مع النقاط المذكورة\n"
            f"- حل المشكلة إن وجدت\n"
            f"- دعوة للعودة أو التواصل"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def respond_batch(self, reviews: str, **kw) -> str:
        """Generate responses for multiple reviews at once.

        Args:
            reviews: Multiple reviews separated by '---'.

        Returns:
            All responses combined as a string.
        """
        system = (
            "خبير إدارة سمعة رقمية ومتخصص في خدمة العملاء. "
            "يرد على التقييمات بطريقة تحول العملاء الغاضبين لمعجبين "
            "وتشجع العملاء الراضين على العودة."
        )
        prompt = (
            f"اكتب ردوداً احترافية على التقييمات التالية:\n\n"
            f"{reviews}\n\n"
            f"لكل تقييم قدم رداً مناسباً ومخصصاً يشمل شكر العميل "
            f"والتعامل مع النقاط المذكورة والإجراء الداخلي المقترح."
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_response_templates(self, business_type: str, **kw) -> str:
        """Generate reusable response templates for common review scenarios.

        Args:
            business_type: Type of business.

        Returns:
            Set of response templates.
        """
        system = (
            "خبير إدارة سمعة رقمية ومتخصص في خدمة العملاء. "
            "يرد على التقييمات بطريقة تحول العملاء الغاضبين لمعجبين "
            "وتشجع العملاء الراضين على العودة."
        )
        prompt = (
            f"أنشئ قوالب ردود جاهزة للتقييمات لنشاط: {business_type}\n\n"
            f"أنشئ قوالب لـ:\n"
            f"- تقييم إيجابي (5 نجوم)\n"
            f"- تقييم جيد (4 نجوم)\n"
            f"- تقييم محايد (3 نجوم)\n"
            f"- تقييم سلبي (2 نجوم)\n"
            f"- تقييم سلبي جداً (نجمة واحدة)\n"
            f"- شكوى عن الخدمة\n"
            f"- شكوى عن السعر\n"
            f"- شكوى عن الجودة"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        review_text: str,
        rating: int,
        business_name: str = "",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a review response and save it to a file."""
        content = self.respond(review_text, rating, business_name, language, **kw)
        return save_output(
            content,
            timestamp_filename("review_response", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="الراد الذكي على التقييمات - إدارة السمعة الرقمية"
    )
    parser.add_argument("--review", required=True, help="نص التقييم")
    parser.add_argument("--rating", type=int, required=True, choices=[1, 2, 3, 4, 5], help="التقييم (1-5)")
    parser.add_argument("--business", default="", help="اسم المنشأة")
    parser.add_argument("--language", default="ar", help="لغة الرد (افتراضي: ar)")

    args = parser.parse_args()
    gen = ReviewResponder()
    print(gen.respond(args.review, args.rating, args.business, args.language))


if __name__ == "__main__":
    main()
