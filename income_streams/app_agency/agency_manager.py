"""AI App Development Agency - Premium Income Stream.

A full automated agency system for building apps/websites with:
- AI-powered project estimation and scoping
- WhatsApp client communication and updates
- Automated progress tracking
- Maintenance contract generation
- Logo and branding as upsells

This is a HIGH-VALUE service: 5,000 - 50,000+ SAR per project

Usage:
    python -m income_streams.app_agency.agency_manager --action new_project
"""

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path

from income_streams.common import AIClient
from income_streams.common.utils import save_json, save_output, timestamp_filename
from income_streams.common.config_loader import get_output_dir


class AgencyManager:
    """Full AI-powered app development agency management system."""

    def __init__(self):
        self.client = AIClient()
        self.projects_dir = get_output_dir("projects")

    def analyze_project_request(self, client_message: str) -> dict:
        """Analyze a client's project request and generate a full proposal.

        Takes the raw client message (from WhatsApp/email) and produces:
        - Project scope breakdown
        - Technology recommendation
        - Timeline estimate
        - Cost estimate
        - Maintenance plan
        """
        system = """أنت مدير مشاريع تقني خبير في شركة تطوير تطبيقات. تحلل طلبات العملاء
وتحولها لعروض أسعار احترافية.

قواعد التسعير (بالريال السعودي):
- تطبيق موبايل بسيط: 5,000-15,000
- تطبيق موبايل متوسط: 15,000-35,000
- تطبيق موبايل معقد: 35,000-80,000
- موقع ويب بسيط: 2,000-5,000
- موقع ويب متقدم: 5,000-20,000
- متجر إلكتروني: 8,000-30,000
- نظام إدارة: 10,000-50,000
- لوقو وهوية بصرية: 500-3,000
- عقد صيانة شهري: 500-2,000

أجب بصيغة JSON فقط."""

        prompt = f"""حلل طلب العميل التالي وأعطني عرض سعر كامل:

رسالة العميل:
{client_message}

أجب بـ JSON بهذا الشكل:
{{
    "project_name": "اسم المشروع",
    "project_type": "نوع المشروع",
    "scope": {{
        "description": "وصف تفصيلي",
        "features": ["ميزة 1", "ميزة 2"],
        "platforms": ["iOS", "Android", "Web"],
        "integrations": ["واتساب", "دفع إلكتروني"]
    }},
    "technology": {{
        "frontend": "التقنية",
        "backend": "التقنية",
        "database": "قاعدة البيانات",
        "hosting": "الاستضافة المقترحة"
    }},
    "timeline": {{
        "phases": [
            {{"name": "التصميم", "duration_days": 7}},
            {{"name": "التطوير", "duration_days": 21}},
            {{"name": "الاختبار", "duration_days": 7}}
        ],
        "total_days": 35
    }},
    "pricing": {{
        "development": 15000,
        "design": 3000,
        "logo": 1500,
        "total": 19500,
        "currency": "SAR",
        "payment_plan": ["50% مقدم", "25% بعد التصميم", "25% عند التسليم"]
    }},
    "maintenance": {{
        "monthly_cost": 800,
        "includes": ["تحديثات أمنية", "نسخ احتياطي", "دعم فني"],
        "contract_months": 12
    }},
    "upsells": ["تسويق رقمي", "SEO", "إدارة سوشال ميديا"]
}}"""

        raw = self.client.generate(prompt, system_prompt=system, max_tokens=3000)

        # Try to parse JSON from response
        try:
            # Find JSON block in response
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0 and end > start:
                return json.loads(raw[start:end])
        except json.JSONDecodeError:
            pass

        return {"raw_analysis": raw}

    def generate_proposal_document(self, project_data: dict) -> str:
        """Generate a professional Arabic proposal document from project data."""
        system = """أنت كاتب عروض أسعار محترف. اكتب عرض سعر رسمي وأنيق بالعربي
لشركة تطوير تطبيقات. العرض يجب أن يكون جاهز للإرسال للعميل."""

        prompt = f"""اكتب عرض سعر احترافي كامل بناءً على هذه البيانات:

{json.dumps(project_data, ensure_ascii=False, indent=2)}

العرض يجب يشمل:
1. مقدمة ترحيبية
2. فهم المشروع
3. نطاق العمل التفصيلي
4. المراحل والجدول الزمني
5. التسعير وخطة الدفع
6. عقد الصيانة
7. لماذا نحن (مميزاتنا)
8. الشروط والأحكام
9. صلاحية العرض (14 يوم)

اكتبه بصيغة Markdown جاهز للتحويل لـ PDF."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_whatsapp_update(self, project_name: str, phase: str, progress: int) -> str:
        """Generate a WhatsApp-friendly project update message."""
        system = "اكتب رسالة واتساب قصيرة واحترافية لتحديث العميل عن مشروعه. استخدم إيموجي باعتدال."

        prompt = f"""اكتب رسالة تحديث واتساب للعميل:
المشروع: {project_name}
المرحلة الحالية: {phase}
نسبة الإنجاز: {progress}%

الرسالة تكون:
- قصيرة ومباشرة
- فيها تفاصيل كافية
- تنتهي بسؤال أو CTA
"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=500)

    def generate_maintenance_contract(self, project_data: dict) -> str:
        """Generate a maintenance contract for ongoing revenue."""
        system = "أنت محامي تقني متخصص في عقود البرمجيات. اكتب عقد صيانة برمجية احترافي بالعربي."

        prompt = f"""اكتب عقد صيانة برمجية بناءً على:
{json.dumps(project_data.get('maintenance', {}), ensure_ascii=False)}

اسم المشروع: {project_data.get('project_name', 'المشروع')}

العقد يشمل:
1. الأطراف
2. نطاق الصيانة
3. مستوى الخدمة (SLA)
4. وقت الاستجابة
5. التسعير والدفع
6. مدة العقد والتجديد
7. الإنهاء
8. حقوق الملكية الفكرية"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def process_full_project(self, client_message: str) -> dict:
        """Full pipeline: analyze -> propose -> save everything."""
        print("1/4 تحليل طلب العميل...")
        analysis = self.analyze_project_request(client_message)

        print("2/4 إنشاء عرض السعر...")
        proposal = self.generate_proposal_document(analysis)

        print("3/4 إنشاء عقد الصيانة...")
        contract = self.generate_maintenance_contract(analysis)

        print("4/4 حفظ الملفات...")
        project_name = analysis.get("project_name", "project")
        ts = datetime.now().strftime("%Y%m%d")

        paths = {
            "analysis": save_json(analysis, f"{ts}_{project_name}_analysis.json", str(self.projects_dir)),
            "proposal": save_output(proposal, f"{ts}_{project_name}_proposal.md", str(self.projects_dir)),
            "contract": save_output(contract, f"{ts}_{project_name}_contract.md", str(self.projects_dir)),
        }

        print(f"\nDone! Files saved to: {self.projects_dir}")
        return {"analysis": analysis, "paths": paths}


def main():
    parser = argparse.ArgumentParser(description="AI App Agency Manager - مدير وكالة التطبيقات")
    parser.add_argument("--analyze", "-a", help="Client message to analyze")
    parser.add_argument("--full", "-f", help="Full pipeline from client message")
    parser.add_argument("--update", "-u", nargs=3, metavar=("PROJECT", "PHASE", "PROGRESS"),
                        help="Generate WhatsApp update")

    args = parser.parse_args()
    agency = AgencyManager()

    if args.full:
        result = agency.process_full_project(args.full)
        print(json.dumps(result["analysis"], ensure_ascii=False, indent=2))
    elif args.analyze:
        result = agency.analyze_project_request(args.analyze)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.update:
        msg = agency.generate_whatsapp_update(args.update[0], args.update[1], int(args.update[2]))
        print(msg)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
