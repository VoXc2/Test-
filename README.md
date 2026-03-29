# AI Income Streams - مصادر دخل بالذكاء الاصطناعي 🤖💰

> منظومة متكاملة من أدوات الذكاء الاصطناعي لتوليد دخل حقيقي وملموس - قابلة للأتمتة بالكامل

---

## ⚡ البدء السريع

```bash
# 1. استنسخ المشروع
git clone <repo-url>
cd Test-

# 2. ثبّت المتطلبات
pip install -r requirements.txt

# 3. أعد إعدادات API
cp .env.example .env
# عدّل .env وأضف مفتاح OpenAI أو Anthropic

# 4. جرّب أي أداة
python -m income_streams.content_generation.blog_generator --topic "الذكاء الاصطناعي" -l ar
python -m prompt_frameworks.runner --list
```

---

## 📊 مصادر الدخل (11 مصدر)

### 🔴 المستوى الأول: دخل سريع (ابدأ اليوم)

| # | المصدر | الدخل المتوقع | السوق | الأمر |
|---|--------|--------------|-------|-------|
| 1 | **كتابة المحتوى** | 500-3,000 ر.س/شهر | خمسات/Fiverr | `python -m income_streams.content_generation.blog_generator` |
| 2 | **الترجمة الذكية** | 1,000-5,000 ر.س/شهر | عربي↔انجليزي | `python -m income_streams.translation_service.translator` |
| 3 | **مولد العروض** | يضاعف فوزك بالمشاريع | فريلانس | `python -m income_streams.freelance_proposals.proposal_generator` |
| 4 | **بناء السير الذاتية** | 50-500 ر.س/سيرة | أفراد+شركات | `python -m income_streams.cv_builder.cv_generator` |

### 🟡 المستوى الثاني: دخل متكرر (اشتراكات شهرية)

| # | المصدر | الدخل المتوقع | السوق | الأمر |
|---|--------|--------------|-------|-------|
| 5 | **أدوات ويب SaaS** | 200-2,000 ر.س/شهر | عالمي | `uvicorn income_streams.micro_saas.app:app` |
| 6 | **متجر البرومبتات** | 500-3,000 ر.س/شهر | عالمي | مكتبة 12+ برومبت جاهزة |
| 7 | **بوت خدمة عملاء واتساب** | 499-1,999 ر.س/عميل/شهر | شركات | `python -m income_streams.whatsapp_support.support_bot` |

### 🟢 المستوى الثالث: دخل عالي القيمة (مشاريع كبيرة)

| # | المصدر | الدخل المتوقع | السوق | الأمر |
|---|--------|--------------|-------|-------|
| 8 | **وكالة تطبيقات AI** | 5,000-80,000 ر.س/مشروع | سعودي+خليجي | `python -m income_streams.app_agency.agency_manager` |
| 9 | **استشارات أعمال واتساب** | 299-1,999 ر.س/عميل/شهر | رواد أعمال | `python -m income_streams.whatsapp_consulting.consulting_bot` |
| 10 | **تحليل عقاري** | 500-2,000 ر.س/تقرير | مستثمرين | `python -m income_streams.real_estate_analyzer.analyzer` |
| 11 | **وثائق قانونية** | 100-2,000 ر.س/وثيقة | شركات+أفراد | `python -m income_streams.legal_documents.legal_generator` |

### 🔵 إضافي: محرك المتاجر الإلكترونية

| # | المصدر | الدخل المتوقع | السوق | الأمر |
|---|--------|--------------|-------|-------|
| + | **أوصاف منتجات المتاجر** | 2-20 ر.س/منتج | 100K+ متجر | `python -m income_streams.ecommerce_engine.product_engine` |

---

## 🧠 أطر العمل الذكية (6 أطر من تغريدات @Mbk8g)

```bash
# عرض جميع الأطر
python -m prompt_frameworks.runner --list

# تشغيل إطار محدد
python -m prompt_frameworks.runner -f career_survival -i "career_description=مهندس برمجيات 5 سنوات"
python -m prompt_frameworks.runner -f deep_thinking -i "problem_statement=كيف أبدأ مشروع تقني"
python -m prompt_frameworks.runner -f opportunity_finder -i "position_description=مطور تطبيقات في الرياض"
```

| # | الإطار | الوصف | المدخلات |
|---|--------|-------|----------|
| 1 | **ماسح بقاء المهنة** | تحليل تعرض وظيفتك للـ AI على طريقة أمودي | `career_description` |
| 2 | **الاستدلال الدستوري** | إجابات مُقيّمة حسب مبادئ Anthropic | `question` |
| 3 | **خريطة تحول الصناعة** | 3 موجات من الاضطراب + خطة 90 يوم | `industry_description` |
| 4 | **التفكير العميق** | حل مشكلات معقدة بأسلوب Princeton | `problem_statement` |
| 5 | **قرار الحياة** | تحليل قرارات كبيرة بمبادئ HHH | `decision` |
| 6 | **مكتشف الفرص** | فرص تقاطع مهاراتك × AI | `position_description` |

---

## 📁 هيكل المشروع

```
Test-/
├── config/                    # إعدادات مركزية
│   ├── settings.yaml          # إعدادات AI والوحدات
│   └── glossary.yaml          # مسرد مصطلحات الترجمة
│
├── income_streams/            # مصادر الدخل
│   ├── common/                # بنية مشتركة (ai_client, config, utils)
│   ├── content_generation/    # 1. كتابة المحتوى
│   ├── translation_service/   # 2. الترجمة الذكية
│   ├── freelance_proposals/   # 3. مولد عروض الفريلانس
│   ├── micro_saas/            # 5. أدوات ويب SaaS
│   ├── prompt_marketplace/    # 6. متجر البرومبتات
│   ├── app_agency/            # 8. وكالة التطبيقات + واتساب
│   ├── whatsapp_consulting/   # 9. استشارات واتساب
│   ├── real_estate_analyzer/  # 10. تحليل عقاري
│   ├── cv_builder/            # 4. بناء السير الذاتية
│   ├── legal_documents/       # 11. وثائق قانونية
│   ├── ecommerce_engine/      # +. أوصاف المنتجات
│   └── whatsapp_support/      # 7. بوت خدمة عملاء
│
├── prompt_frameworks/         # أطر العمل الـ 6
│   ├── runner.py              # CLI لتشغيل أي إطار
│   ├── base_framework.py      # الفئة الأساسية
│   ├── templates/             # قوالب YAML
│   └── *.py                   # الأطر الـ 6
│
├── tests/                     # اختبارات
├── .env.example               # نموذج المتغيرات
└── requirements.txt           # المتطلبات
```

---

## 🛠 أمثلة الاستخدام التفصيلية

### كتابة مقال SEO
```bash
python -m income_streams.content_generation.blog_generator \
  --topic "أفضل 10 تطبيقات ذكاء اصطناعي للأعمال" \
  --language ar --tone professional --words 1500 --save
```

### ترجمة ملف كامل
```bash
python -m income_streams.translation_service.translator \
  --file document.txt --from en --to ar --domain technical
```

### تحليل عقاري
```bash
python -m income_streams.real_estate_analyzer.analyzer \
  --type investment --location "الرياض - حي العليا" \
  --property-type تجاري --budget "2 مليون ريال"
```

### مولد عروض سعر المشاريع (وكالة التطبيقات)
```bash
python -m income_streams.app_agency.agency_manager \
  --full "أبي تطبيق توصيل طلبات مطاعم مثل هنقرستيشن بس لمدينتي فقط"
```

### إنشاء عقد قانوني
```bash
python -m income_streams.legal_documents.legal_generator \
  --type employment --party1 "شركة ABC" --party2 "محمد أحمد" \
  --details "عقد عمل سنوي، راتب 15000 ريال" --save
```

### إنشاء بوت خدمة عملاء لمطعم
```bash
python -m income_streams.whatsapp_support.support_bot \
  --setup "مطعم برجر في الرياض، توصيل وطلبات محل، قائمة 30 صنف"
```

### بناء سيرة ذاتية كاملة
```bash
python -m income_streams.cv_builder.cv_generator \
  --name "أحمد محمد" --title "مطور Full Stack" \
  --experience "3 سنوات في React و Node.js" \
  --skills "JavaScript, Python, AWS" --full-package
```

### تشغيل أدوات الويب
```bash
uvicorn income_streams.micro_saas.app:app --host 0.0.0.0 --port 8000
# افتح http://localhost:8000
```

---

## ⚙️ الإعدادات

### مفاتيح API (ملف `.env`)
```bash
OPENAI_API_KEY=sk-...        # مفتاح OpenAI (الأساسي)
ANTHROPIC_API_KEY=sk-ant-... # مفتاح Anthropic (بديل)
AI_PROVIDER=openai            # openai أو anthropic
AI_MODEL=gpt-4o-mini          # الموديل الافتراضي (أرخص وأسرع)
```

### تغيير الموديل
عدّل `config/settings.yaml` لتغيير الموديل لكل وحدة:
```yaml
ai:
  default_model: gpt-4o-mini  # الافتراضي (رخيص)
  overrides:
    translation_service:
      model: gpt-4o            # أعلى جودة للترجمة
    prompt_frameworks:
      model: gpt-4o            # أعلى جودة للأطر
```

---

## 💡 خارطة الطريق للربح

### الأسبوع 1: ابدأ بالدخل السريع
1. سجّل على خمسات/مستقل/Fiverr
2. اعرض خدمات: كتابة محتوى، ترجمة، سير ذاتية
3. استخدم مولد العروض لتقديم على المشاريع

### الأسبوع 2: ابنِ الدخل المتكرر
4. انشر أدوات الويب على سيرفر (Render/Railway مجاني)
5. اعرض بوتات واتساب للمطاعم والمتاجر القريبة
6. ابدأ بمتجر البرومبتات على Gumroad

### الأسبوع 3-4: ارتقِ للمشاريع الكبيرة
7. اعرض خدمة وكالة التطبيقات
8. ابدأ خدمة الاستشارات عبر واتساب
9. اعرض التحليل العقاري والوثائق القانونية

---

## 📋 المتطلبات

- Python 3.10+
- مفتاح API من OpenAI أو Anthropic
- اتصال إنترنت

---

## ⚠️ تنويهات مهمة

- **الوثائق القانونية**: نماذج أولية يجب مراجعتها من محامي مرخص
- **التحليل العقاري**: تحليلات تقديرية وليست نصيحة استثمارية رسمية
- **الاستشارات**: الأداة مساعدة وليست بديلاً عن مستشار متخصص
- **تكاليف API**: راقب استهلاكك من خلال لوحة تحكم OpenAI/Anthropic
