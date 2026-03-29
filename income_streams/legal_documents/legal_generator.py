"""AI Legal Document Generator - Arabic Contracts & Agreements.

Generate professional legal documents in Arabic compliant with Saudi law.
DISCLAIMER: These are templates and should be reviewed by a licensed lawyer.

Business Model:
- Single document: 100-500 SAR
- Monthly package for businesses: 999 SAR/month (10 docs)
- Customization service: 500-2000 SAR per document

Usage:
    python -m income_streams.legal_documents.legal_generator --type employment --parties "شركة ABC" "محمد أحمد"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.utils import save_output, timestamp_filename
from income_streams.common.config_loader import get_output_dir


class LegalDocumentGenerator:
    """Generate Arabic legal documents and contracts."""

    DOCUMENT_TYPES = {
        "employment": "عقد عمل",
        "freelance": "عقد عمل حر",
        "service": "عقد تقديم خدمات",
        "nda": "اتفاقية سرية",
        "partnership": "عقد شراكة",
        "rental": "عقد إيجار",
        "sale": "عقد بيع",
        "agency": "عقد وكالة",
        "maintenance": "عقد صيانة",
        "consulting": "عقد استشارات",
        "ecommerce_terms": "شروط وأحكام متجر إلكتروني",
        "privacy_policy": "سياسة خصوصية",
    }

    def __init__(self):
        self.client = AIClient()

    def generate(
        self,
        doc_type: str,
        party_1: str = "الطرف الأول",
        party_2: str = "الطرف الثاني",
        details: str = "",
        language: str = "ar",
    ) -> str:
        """Generate a legal document.

        Args:
            doc_type: Type from DOCUMENT_TYPES
            party_1: First party name/description
            party_2: Second party name/description
            details: Additional details/requirements
            language: 'ar' or 'en'
        """
        doc_name = self.DOCUMENT_TYPES.get(doc_type, doc_type)
        lang = "Arabic" if language == "ar" else "English"

        system = f"""أنت محامي سعودي خبير في صياغة العقود والوثائق القانونية.
تكتب بـ{lang} مع مراعاة:
- نظام العمل السعودي
- نظام المعاملات المدنية
- نظام التجارة الإلكترونية
- أنظمة وزارة التجارة

تنويه مهم: هذا نموذج أولي يجب مراجعته من محامي مرخص قبل الاستخدام.

اكتب العقد بصيغة رسمية قانونية كاملة."""

        prompt = f"""اكتب {doc_name} كامل ومفصل:

الطرف الأول: {party_1}
الطرف الثاني: {party_2}
تفاصيل إضافية: {details or 'لا يوجد'}

العقد يشمل:
1. البسملة والتاريخ (هجري وميلادي)
2. تعريف الأطراف
3. التمهيد
4. البنود والشروط (مفصلة ومرقمة)
5. الالتزامات المالية
6. مدة العقد والتجديد
7. الإنهاء والفسخ
8. السرية
9. القوة القاهرة
10. حل النزاعات (الجهة المختصة)
11. أحكام عامة
12. التوقيعات

أضف بنوداً خاصة بنوع العقد ({doc_name}).
اكتب عقداً شاملاً لا يقل عن 15 بنداً."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_terms_of_service(self, business_name: str, business_type: str) -> str:
        """Generate Terms of Service for a website/app."""
        system = "أنت محامي متخصص في قانون التجارة الإلكترونية السعودي."

        prompt = f"""اكتب شروط وأحكام شاملة لـ:
الاسم: {business_name}
النوع: {business_type}

تشمل: شروط الاستخدام، سياسة الإرجاع، المسؤولية، حقوق الملكية الفكرية،
الخصوصية، ملفات الكوكيز، القانون الحاكم (سعودي)."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def review_contract(self, contract_text: str) -> str:
        """Review an existing contract and provide feedback."""
        system = """أنت محامي مراجعة عقود. حلل العقد وأبرز:
- الثغرات القانونية
- البنود الناقصة
- المخاطر على كل طرف
- التوصيات"""

        prompt = f"""راجع هذا العقد:

{contract_text}

أعطني:
1. ملخص العقد
2. نقاط القوة
3. الثغرات والنقص
4. المخاطر القانونية
5. التوصيات التفصيلية
6. البنود المقترح إضافتها"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_and_save(self, doc_type: str, **kwargs) -> str:
        """Generate and save document."""
        content = self.generate(doc_type, **kwargs)
        output_dir = get_output_dir("reports")
        filename = timestamp_filename(f"legal_{doc_type}", "md")
        return save_output(content, filename, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="Legal Document Generator - مولد الوثائق القانونية")
    parser.add_argument("--type", "-t", required=True,
                        choices=list(LegalDocumentGenerator.DOCUMENT_TYPES.keys()),
                        help="Document type")
    parser.add_argument("--party1", "-p1", default="الطرف الأول", help="First party")
    parser.add_argument("--party2", "-p2", default="الطرف الثاني", help="Second party")
    parser.add_argument("--details", "-d", default="", help="Additional details")
    parser.add_argument("--save", "-s", action="store_true")

    args = parser.parse_args()
    gen = LegalDocumentGenerator()

    if args.save:
        path = gen.generate_and_save(args.type, party_1=args.party1, party_2=args.party2, details=args.details)
        print(f"Saved to: {path}")
    else:
        result = gen.generate(args.type, party_1=args.party1, party_2=args.party2, details=args.details)
        print(result)


if __name__ == "__main__":
    main()
