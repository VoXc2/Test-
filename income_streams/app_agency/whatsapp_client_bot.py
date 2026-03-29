"""WhatsApp Client Communication Bot.

Automated client communication for the app agency via WhatsApp Business API.
Handles: inquiries, updates, feedback collection, payment reminders.

This integrates with WhatsApp Business API (or can use Twilio/Vonage).
"""

from income_streams.common import AIClient


class WhatsAppClientBot:
    """AI-powered WhatsApp bot for client management."""

    def __init__(self):
        self.client = AIClient()

    def handle_inquiry(self, message: str) -> str:
        """Handle a new client inquiry via WhatsApp."""
        system = """أنت مساعد مبيعات ذكي لشركة تطوير تطبيقات. ترد على استفسارات العملاء عبر الواتساب.

قواعدك:
- كن ودوداً واحترافياً
- اسأل أسئلة ذكية لفهم احتياج العميل
- لا تعطي سعر نهائي، قل "نحتاج نفهم المشروع أكثر"
- وجّه العميل لحجز اجتماع مجاني
- الرسائل قصيرة ومناسبة للواتساب
- استخدم إيموجي باعتدال"""

        prompt = f"رسالة العميل: {message}\n\nرد عليه:"
        return self.client.generate(prompt, system_prompt=system, max_tokens=500)

    def handle_feedback(self, project_name: str, client_feedback: str) -> str:
        """Process client feedback and generate appropriate response."""
        system = """أنت مدير مشاريع يتعامل مع ملاحظات العملاء. كن إيجابياً ومتفهماً
وقدم حلول عملية. الرسائل للواتساب (قصيرة)."""

        prompt = f"""المشروع: {project_name}
ملاحظات العميل: {client_feedback}

اكتب:
1. رد واتساب للعميل (إيجابي ومتفهم)
2. قائمة مهام داخلية (ما يجب تعديله)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=800)

    def generate_payment_reminder(self, client_name: str, amount: float, due_date: str) -> str:
        """Generate a polite payment reminder message."""
        system = "اكتب رسالة واتساب مهذبة لتذكير العميل بالدفعة المستحقة. كن لطيفاً وغير ضاغط."

        prompt = f"""العميل: {client_name}
المبلغ: {amount} ريال
تاريخ الاستحقاق: {due_date}

اكتب رسالة تذكير لطيفة."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=300)

    def generate_project_completion(self, project_name: str, deliverables: list) -> str:
        """Generate project completion message with next steps."""
        system = "اكتب رسالة واتساب احترافية لإبلاغ العميل بإتمام المشروع."

        deliverables_text = "\n".join(f"- {d}" for d in deliverables)
        prompt = f"""المشروع: {project_name}
المخرجات:
{deliverables_text}

اكتب رسالة تشمل:
1. تهنئة بإتمام المشروع
2. قائمة المخرجات
3. عرض عقد الصيانة
4. طلب تقييم/شهادة"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=500)

    def classify_message(self, message: str) -> dict:
        """Classify incoming WhatsApp message intent."""
        system = """صنف رسالة العميل لأحد هذه الأنواع وأجب بـ JSON فقط:
- inquiry: استفسار عن خدمة جديدة
- feedback: ملاحظات على مشروع قائم
- support: طلب دعم فني
- payment: سؤال عن الدفع
- other: غير ذلك"""

        prompt = f'رسالة العميل: "{message}"\n\nJSON:'
        raw = self.client.generate(prompt, system_prompt=system, max_tokens=200)

        import json
        try:
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0:
                return json.loads(raw[start:end])
        except json.JSONDecodeError:
            pass
        return {"type": "other", "raw": raw}
