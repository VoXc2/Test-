"""AI Customer Support WhatsApp Automation.

Deploy AI-powered customer support bots for businesses via WhatsApp.
The bot handles FAQs, order tracking, complaints, and escalation.

Business Model:
- Setup fee: 2,000-5,000 SAR
- Monthly: 499-1,999 SAR depending on volume
- Per business = recurring revenue
- Target: restaurants, clinics, stores, service providers

Usage:
    python -m income_streams.whatsapp_support.support_bot --business "مطعم" --query "وين الطلب حقي؟"
"""

import argparse
import json

from income_streams.common import AIClient
from income_streams.common.utils import save_output, save_json
from income_streams.common.config_loader import get_output_dir


class CustomerSupportBot:
    """AI customer support bot configurable for any business."""

    def __init__(self, business_name: str = "", business_type: str = "",
                 knowledge_base: str = ""):
        self.client = AIClient()
        self.business_name = business_name
        self.business_type = business_type
        self.knowledge_base = knowledge_base

    def respond(self, customer_message: str) -> str:
        """Generate a response to a customer message."""
        kb_section = ""
        if self.knowledge_base:
            kb_section = "معلومات الشركة:\n" + self.knowledge_base

        system = f"""أنت موظف خدمة عملاء ذكي لـ {self.business_name or 'الشركة'} ({self.business_type or 'أعمال'}).

قواعدك:
- رد بأسلوب ودود واحترافي
- الرسائل قصيرة ومناسبة للواتساب
- حل المشكلة أو وجّه للشخص المناسب
- لا تخترع معلومات غير موجودة
- إذا ما تعرف الجواب قل "خلني أحولك لفريقنا المختص"
- استخدم إيموجي باعتدال

{kb_section}"""

        return self.client.generate(customer_message, system_prompt=system, max_tokens=500)

    def generate_knowledge_base(self, business_description: str) -> str:
        """Generate an initial knowledge base/FAQ for a business."""
        system = "أنت خبير خدمة عملاء. أنشئ قاعدة معرفة شاملة لبوت الدعم."

        prompt = f"""أنشئ قاعدة معرفة لبوت خدمة العملاء:

الشركة: {business_description}

أنشئ:
1. **أسئلة شائعة** (15-20 سؤال مع أجوبة)
   - عن الخدمة/المنتج
   - عن الأسعار
   - عن الدفع
   - عن التوصيل/الاستلام
   - عن الإرجاع/الاستبدال
   - عن ساعات العمل
   - عن التواصل

2. **سيناريوهات التعامل**
   - عميل غاضب
   - استفسار عام
   - شكوى
   - طلب خصم
   - مشكلة تقنية

3. **ردود جاهزة** (10 ردود)
   - رسالة ترحيب
   - رسالة خارج أوقات العمل
   - رسالة تأكيد الطلب
   - رسالة تحويل لموظف
   - وغيرها

اكتبها بصيغة YAML."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def setup_business(self, business_description: str) -> dict:
        """Full setup for a new business client."""
        print("1/3 إنشاء قاعدة المعرفة...")
        kb = self.generate_knowledge_base(business_description)

        print("2/3 إنشاء رسائل الترحيب...")
        welcome = self.client.generate(
            f"اكتب 3 رسائل واتساب ترحيبية مختلفة لـ: {business_description}",
            max_tokens=500,
        )

        print("3/3 إنشاء دليل التشغيل...")
        guide = self.client.generate(
            f"""اكتب دليل تشغيل بوت الواتساب لصاحب العمل:
{business_description}

يشمل: كيف يعمل، كيف يعدّله، متى يتدخل يدوياً، أفضل الممارسات""",
            max_tokens=2000,
        )

        output_dir = get_output_dir("projects")
        results = {
            "knowledge_base": save_output(kb, "knowledge_base.yaml", str(output_dir)),
            "welcome_messages": save_output(welcome, "welcome_messages.md", str(output_dir)),
            "operations_guide": save_output(guide, "operations_guide.md", str(output_dir)),
        }

        print(f"\nSetup complete! Files in: {output_dir}")
        return results

    def analyze_conversations(self, conversations_text: str) -> str:
        """Analyze customer conversations for insights."""
        system = "أنت محلل تجربة عملاء. حلل المحادثات واستخرج رؤى عملية."

        prompt = f"""حلل محادثات خدمة العملاء التالية:

{conversations_text}

أعطني:
1. الأسئلة الأكثر تكراراً
2. المشاكل الشائعة
3. معدل رضا العملاء (تقدير)
4. نقاط التحسين
5. توصيات لتحسين الخدمة
6. أسئلة يجب إضافتها للـ FAQ"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)


def main():
    parser = argparse.ArgumentParser(description="Customer Support Bot - بوت خدمة العملاء")
    parser.add_argument("--business", "-b", default="", help="Business name")
    parser.add_argument("--type", "-t", default="", help="Business type")
    parser.add_argument("--query", "-q", help="Customer message to respond to")
    parser.add_argument("--setup", "-s", help="Setup new business (description)")
    parser.add_argument("--generate-kb", help="Generate knowledge base")

    args = parser.parse_args()
    bot = CustomerSupportBot(business_name=args.business, business_type=args.type)

    if args.setup:
        bot.setup_business(args.setup)
    elif args.generate_kb:
        print(bot.generate_knowledge_base(args.generate_kb))
    elif args.query:
        print(bot.respond(args.query))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
