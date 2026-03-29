"""SEO Content Optimizer - Income Stream #60.
Business Model: تحسين محركات البحث وإنشاء محتوى متوافق مع SEO ($300 - $3,000 لكل مشروع)
Usage: python -m income_streams.seo_optimizer.seo_engine --topic "الموضوع" --keywords "كلمات مفتاحية" --type blog --save
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import save_output, timestamp_filename


class SEOContentOptimizer:
    """AI-powered SEO content generation and optimization system."""

    def __init__(self):
        self.client = AIClient(module_name="seo_optimizer")

    def generate(self, topic: str, keywords: str = "", content_type: str = "blog", language: str = "ar") -> str:
        """Generate fully SEO-optimized content with metadata, headings, and schema markup.

        Args:
            topic: The main topic or subject for the content.
            keywords: Comma-separated target keywords (optional, AI will suggest if empty).
            content_type: Type of content - blog, product_page, service_page, or pillar_page.
            language: Output language (ar for Arabic, en for English).
        """
        system = (
            "أنت متخصص في تحسين محركات البحث (SEO Specialist) بخبرة تتجاوز 10 سنوات في ترتيب "
            "المحتوى العربي والإنجليزي على صفحات جوجل الأولى. خبير في معايير E-E-A-T "
            "(Experience, Expertise, Authoritativeness, Trustworthiness)، والـ Semantic SEO، "
            "وسلوك البحث في منطقة الشرق الأوسط وشمال أفريقيا. حققت نتائج مثبتة: زيادة الزيارات "
            "العضوية بنسبة 300%+ لأكثر من 40 موقعًا عربيًا في مجالات التجارة الإلكترونية، "
            "التعليم، والخدمات المهنية. تفهم خوارزميات جوجل الحديثة بما فيها Helpful Content Update "
            "وCore Web Vitals. متخصص في بناء محتوى يرضي المستخدم والخوارزمية معًا، "
            "مع التركيز على نية البحث (search intent) وتجربة المستخدم. أجب بمحتوى احترافي "
            "ومنظم وجاهز للنشر مباشرة."
        )

        content_types = {
            "blog": "مقال مدونة شامل (1500+ كلمة) - معلوماتي وتثقيفي",
            "product_page": "صفحة منتج محسّنة - تجارية وبيعية مع مواصفات تقنية",
            "service_page": "صفحة خدمة - تعريفية وبيعية مع إثبات اجتماعي",
            "pillar_page": "صفحة ركيزة (Pillar Page) - دليل شامل (3000+ كلمة) مع روابط داخلية",
        }
        type_desc = content_types.get(content_type, content_types["blog"])

        keywords_section = f"الكلمات المفتاحية المستهدفة: {keywords}" if keywords else "اقترح الكلمات المفتاحية المناسبة بناءً على الموضوع ونية البحث"

        lang_instruction = "اكتب المحتوى بالكامل باللغة العربية مع مراعاة قواعد SEO للمحتوى العربي." if language == "ar" else "Write all content in English following SEO best practices."

        prompt = f"""أنشئ محتوى متوافق بالكامل مع SEO للموضوع التالي:

الموضوع: {topic}
نوع المحتوى: {content_type} ({type_desc})
{keywords_section}
{lang_instruction}

أريد محتوى SEO شامل يتضمن جميع العناصر التالية:

## 1. علامة العنوان (Title Tag)
- عنوان محسّن لا يتجاوز 60 حرفًا
- يتضمن الكلمة المفتاحية الرئيسية
- جذاب للنقر (CTR optimization)
- 3 خيارات بديلة

## 2. الوصف التعريفي (Meta Description)
- وصف مقنع لا يتجاوز 155 حرفًا
- يتضمن الكلمة المفتاحية والـ CTA
- 3 خيارات بديلة

## 3. هيكل العناوين مع الكلمات المفتاحية (H1-H3 Structure)
- H1 رئيسي واحد (يختلف عن Title Tag)
- H2 عناوين فرعية (5-8 عناوين)
- H3 عناوين فرعية تفصيلية تحت كل H2
- توزيع طبيعي للكلمات المفتاحية في العناوين

## 4. المحتوى الكامل (Full Body Content - 1500+ كلمة)
- مقدمة جذابة تتضمن الكلمة المفتاحية في أول 100 كلمة
- فقرات منظمة ومتسلسلة منطقيًا
- استخدام LSI keywords بشكل طبيعي
- قوائم نقطية ومرقمة لسهولة القراءة
- جداول مقارنة عند الحاجة
- إحصائيات ومصادر موثوقة
- خاتمة قوية مع CTA
- كثافة الكلمات المفتاحية 1-2% بشكل طبيعي

## 5. اقتراحات الروابط الداخلية (Internal Linking Suggestions)
- 5-8 مواضيع مقترحة للربط الداخلي
- نص الرابط (anchor text) المقترح لكل رابط
- موضع الرابط المثالي في المحتوى

## 6. توصيات Schema Markup (JSON-LD)
- كود JSON-LD كامل وجاهز للنسخ
- نوع الـ Schema المناسب (Article, Product, Service, FAQPage, HowTo)
- جميع الحقول المطلوبة والمقترحة
- FAQ Schema إذا كان المحتوى يتضمن أسئلة شائعة

## 7. اقتراحات النص البديل للصور (Image Alt Text)
- 5-8 اقتراحات لصور مناسبة للمحتوى
- نص بديل (alt text) محسّن لكل صورة
- اسم ملف مقترح لكل صورة (SEO-friendly filename)
- وصف للتعليق التوضيحي (caption)

## 8. تحسين المقتطفات المميزة (Featured Snippet Optimization)
- فقرة تعريفية (paragraph snippet) - 40-60 كلمة
- قائمة مرقمة (list snippet) - خطوات أو عناصر
- جدول (table snippet) - إذا كان مناسبًا
- تنسيق "People Also Ask" - 5 أسئلة مع إجابات مختصرة

## 9. الكلمات المفتاحية ذات الصلة (Related Keywords)
- 15-20 كلمة مفتاحية ذات صلة مع حجم البحث التقديري
- تصنيفها: رئيسية، ثانوية، طويلة الذيل (long-tail)
- نية البحث لكل كلمة (معلوماتية، تجارية، ملاحية، تحويلية)
- اقتراحات لمحتوى مستقبلي بناءً على الكلمات المفتاحية

اجعل المحتوى عالي الجودة، فريدًا، ومفيدًا للقارئ أولًا ومتوافقًا مع محركات البحث ثانيًا."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_keyword_strategy(self, niche: str, num_keywords: int = 20, language: str = "ar") -> str:
        """Generate a keyword cluster strategy for a niche.

        Args:
            niche: The niche or industry to research keywords for.
            num_keywords: Number of keyword clusters to generate.
            language: Output language.
        """
        system = (
            "أنت خبير أبحاث كلمات مفتاحية متخصص في السوق العربي مع فهم عميق لسلوك البحث "
            "في منطقة MENA. تستخدم منهجية Keyword Clustering وTopical Authority لبناء "
            "استراتيجيات محتوى تهيمن على نتائج البحث. خبير في أدوات مثل Ahrefs، SEMrush، "
            "وGoogle Keyword Planner مع تركيز خاص على الكلمات المفتاحية العربية وتحدياتها "
            "(الاختلافات اللهجية، التشكيل، الترجمة بين العامية والفصحى)."
        )

        lang_instruction = "اكتب الاستراتيجية باللغة العربية." if language == "ar" else "Write the strategy in English."

        prompt = f"""ابنِ استراتيجية كلمات مفتاحية شاملة للمجال التالي:

المجال/النيتش: {niche}
عدد مجموعات الكلمات المفتاحية: {num_keywords}
{lang_instruction}

لكل مجموعة كلمات مفتاحية (Keyword Cluster) قدم:

1. **الكلمة المفتاحية الرئيسية** (Seed Keyword)
2. **حجم البحث التقديري** (شهريًا)
3. **صعوبة المنافسة** (منخفضة/متوسطة/عالية)
4. **نية البحث** (معلوماتية/تجارية/ملاحية/تحويلية)
5. **5 كلمات مفتاحية فرعية** (Long-tail variations)
6. **نوع المحتوى المقترح** (مقال، صفحة منتج، دليل، مقارنة، إلخ)
7. **أولوية الاستهداف** (عالية/متوسطة/منخفضة)

ثم قدم:
- **خريطة المحتوى** (Content Map) توضح كيف ترتبط المجموعات ببعضها
- **جدول نشر مقترح** (أي مجموعة تُنشر أولًا ولماذا)
- **فرص المقتطفات المميزة** (Featured Snippet opportunities)
- **تحليل الفجوة** (Content Gap) - مواضيع يغفلها المنافسون

رتب المجموعات حسب الأولوية (أسهل للترتيب + أعلى عائد أولًا)."""

        return self.client.generate(prompt, system_prompt=system, max_tokens=4000)

    def generate_and_save(self, topic: str, keywords: str = "", content_type: str = "blog", language: str = "ar") -> str:
        """Generate SEO-optimized content and save to file.

        Returns:
            Path to the saved file.
        """
        content = self.generate(topic, keywords, content_type, language)
        filename = timestamp_filename("seo_content", "md")
        return save_output(content, filename, str(get_output_dir("seo_optimizer")))


def main():
    parser = argparse.ArgumentParser(description="SEO Content Optimizer - محسّن محتوى محركات البحث")
    parser.add_argument("--topic", "-t", required=True, help="Main topic or subject")
    parser.add_argument("--keywords", "-k", default="",
                        help="Comma-separated target keywords (optional)")
    parser.add_argument("--type", "-y", choices=["blog", "product_page", "service_page", "pillar_page"],
                        default="blog", help="Content type (default: blog)")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"],
                        help="Output language (default: ar)")
    parser.add_argument("--keyword-strategy", "-ks", metavar="NICHE",
                        help="Generate keyword cluster strategy for a niche instead of content")
    parser.add_argument("--num-keywords", "-n", type=int, default=20,
                        help="Number of keyword clusters for strategy (default: 20)")
    parser.add_argument("--save", "-s", action="store_true", help="Save output to file")

    args = parser.parse_args()
    gen = SEOContentOptimizer()

    if args.keyword_strategy:
        content = gen.generate_keyword_strategy(args.keyword_strategy, args.num_keywords, args.language)
        print(content)
    elif args.save:
        path = gen.generate_and_save(args.topic, args.keywords, args.type, args.language)
        print(f"تم الحفظ: {path}")
    else:
        print(gen.generate(args.topic, args.keywords, args.type, args.language))


if __name__ == "__main__":
    main()
