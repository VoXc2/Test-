"""AI-powered tax guide for Saudi and GCC tax systems."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class TaxGuide:
    """Generate comprehensive tax guides for Saudi Arabia and GCC countries.

    تنويه: هذا دليل عام وليس استشارة ضريبية رسمية. يرجى الرجوع لمحاسب قانوني معتمد.
    """

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        business_type: str,
        revenue: float,
        country: str = "SA",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a comprehensive tax guide.

        Args:
            business_type: Type of business or activity.
            revenue: Annual revenue amount.
            country: Country code (SA/AE/KW).
            language: Output language (default Arabic).

        Returns:
            Detailed tax guide as a string.
        """
        system = (
            "مستشار ضريبي خبير في النظام الضريبي السعودي (ZATCA). "
            "يفهم ضريبة القيمة المضافة، الزكاة، ضريبة الدخل، والاستقطاع. "
            "ليس بديلاً عن محاسب قانوني. "
            "يقدم: الضرائب المطبقة، كيفية الحساب، مواعيد التقديم، الإعفاءات، "
            "نصائح التوفير الضريبي، المستندات المطلوبة، الغرامات المحتملة."
        )
        prompt = (
            f"أنشئ دليلاً ضريبياً شاملاً للحالة التالية:\n\n"
            f"نوع النشاط: {business_type}\n"
            f"الإيرادات السنوية: {revenue} ريال\n"
            f"الدولة: {country}\n"
            f"اللغة: {language}\n\n"
            f"يجب أن يشمل الدليل:\n"
            f"- الضرائب المطبقة على هذا النشاط\n"
            f"- كيفية حساب كل ضريبة\n"
            f"- مواعيد التقديم والسداد\n"
            f"- الإعفاءات المتاحة\n"
            f"- نصائح للتوفير الضريبي القانوني\n"
            f"- المستندات المطلوبة للتسجيل والإقرارات\n"
            f"- الغرامات المحتملة عند التأخير\n\n"
            f"⚠️ تنويه: هذا دليل عام وليس استشارة ضريبية رسمية."
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def vat_calculator(self, amount: float, inclusive: bool = False) -> str:
        """Calculate VAT for a given amount.

        Args:
            amount: The amount (inclusive or exclusive of VAT).
            inclusive: If True, amount already includes VAT.

        Returns:
            Formatted VAT calculation breakdown.
        """
        rate = 15
        if inclusive:
            base_amount = amount / (1 + rate / 100)
            vat_amount = amount - base_amount
            total = amount
        else:
            base_amount = amount
            vat_amount = amount * (rate / 100)
            total = amount + vat_amount
        return (
            f"المبلغ قبل الضريبة: {base_amount:,.2f} ريال\n"
            f"نسبة ضريبة القيمة المضافة: {rate}%\n"
            f"مبلغ الضريبة: {vat_amount:,.2f} ريال\n"
            f"الإجمالي شامل الضريبة: {total:,.2f} ريال"
        )

    def generate_and_save(
        self,
        business_type: str,
        revenue: float,
        country: str = "SA",
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a tax guide and save it to a file."""
        content = self.generate(business_type, revenue, country, language, **kw)
        return save_output(
            content,
            timestamp_filename("tax_guide", "md"),
            str(get_output_dir("reports")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="الدليل الضريبي الشامل - ZATCA وضريبة القيمة المضافة"
    )
    parser.add_argument("--business-type", dest="business_type", required=True, help="نوع النشاط التجاري")
    parser.add_argument("--revenue", type=float, required=True, help="الإيرادات السنوية بالريال")
    parser.add_argument(
        "--country",
        choices=["SA", "AE", "BH", "KW", "OM", "QA"],
        default="SA",
        help="الدولة (افتراضي: SA)",
    )
    parser.add_argument("--save", action="store_true", help="حفظ الدليل في ملف")

    args = parser.parse_args()
    gen = TaxGuide()

    if args.save:
        path = gen.generate_and_save(args.business_type, args.revenue, args.country)
        print(f"تم حفظ الدليل الضريبي في: {path}")
    else:
        print(gen.generate(args.business_type, args.revenue, args.country))


if __name__ == "__main__":
    main()
