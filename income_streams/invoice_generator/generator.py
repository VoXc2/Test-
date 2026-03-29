"""AI-powered invoice generator compliant with ZATCA and Saudi VAT requirements."""

import argparse

from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class InvoiceGenerator:
    """Generate professional invoices compliant with Saudi VAT and ZATCA regulations."""

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        from_company: str,
        to_client: str,
        items: str,
        tax_rate: float = 15,
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate a professional invoice.

        Args:
            from_company: Seller company name and details.
            to_client: Buyer/client name and details.
            items: Items in format "خدمة1:500,خدمة2:300".
            tax_rate: VAT tax rate percentage (default 15%).
            language: Output language (default Arabic).

        Returns:
            Formatted invoice as a string.
        """
        system = (
            "محاسب معتمد خبير في متطلبات ZATCA والفوترة الإلكترونية السعودية. "
            "ينشئ فواتير احترافية متوافقة مع ضريبة القيمة المضافة. "
            "الفاتورة تشمل: رقم الفاتورة، التاريخ، بيانات البائع/المشتري، "
            "جدول البنود (الوصف+الكمية+السعر+الضريبة+الإجمالي)، المجموع الفرعي، "
            "ضريبة القيمة المضافة، الإجمالي، شروط الدفع، الرقم الضريبي."
        )
        prompt = (
            f"أنشئ فاتورة احترافية متوافقة مع ZATCA بالتفاصيل التالية:\n\n"
            f"البائع: {from_company}\n"
            f"المشتري: {to_client}\n"
            f"البنود: {items}\n"
            f"نسبة ضريبة القيمة المضافة: {tax_rate}%\n"
            f"اللغة: {language}\n\n"
            f"يجب أن تشمل الفاتورة:\n"
            f"- رقم فاتورة فريد وتاريخ الإصدار\n"
            f"- بيانات البائع والمشتري كاملة مع الرقم الضريبي\n"
            f"- جدول البنود مع الوصف والكمية والسعر والضريبة والإجمالي\n"
            f"- المجموع الفرعي وضريبة القيمة المضافة {tax_rate}% والإجمالي النهائي\n"
            f"- شروط الدفع والملاحظات"
        )
        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(
        self,
        from_company: str,
        to_client: str,
        items: str,
        tax_rate: float = 15,
        language: str = "ar",
        **kw,
    ) -> str:
        """Generate an invoice and save it to a file."""
        content = self.generate(from_company, to_client, items, tax_rate, language, **kw)
        return save_output(
            content,
            timestamp_filename("invoice", "md"),
            str(get_output_dir("invoices")),
        )


def main():
    parser = argparse.ArgumentParser(
        description="مولد الفواتير الاحترافية - متوافق مع ZATCA وضريبة القيمة المضافة"
    )
    parser.add_argument("--from", dest="from_company", required=True, help="اسم وبيانات الشركة البائعة")
    parser.add_argument("--to", required=True, help="اسم وبيانات العميل/المشتري")
    parser.add_argument("--items", required=True, help="البنود بصيغة: خدمة1:500,خدمة2:300")
    parser.add_argument("--tax", type=float, default=15, help="نسبة ضريبة القيمة المضافة (افتراضي: 15)")
    parser.add_argument("--save", action="store_true", help="حفظ الفاتورة في ملف")

    args = parser.parse_args()
    gen = InvoiceGenerator()

    if args.save:
        path = gen.generate_and_save(args.from_company, args.to, args.items, args.tax)
        print(f"تم حفظ الفاتورة في: {path}")
    else:
        print(gen.generate(args.from_company, args.to, args.items, args.tax))


if __name__ == "__main__":
    main()
