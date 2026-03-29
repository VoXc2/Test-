"""AI E-commerce Product Description Engine.

Generate compelling product descriptions, titles, and SEO content
for online stores (Salla, Zid, Shopify, Amazon).

Business Model:
- Per product: 5-20 SAR
- Bulk (100+ products): 2-5 SAR each
- Monthly for stores: 499-999 SAR (unlimited)
- Huge market: 100,000+ online stores in Saudi alone

Usage:
    python -m income_streams.ecommerce_engine.product_engine --product "ساعة ذكية رياضية"
"""

import argparse

from income_streams.common import AIClient
from income_streams.common.utils import save_output, timestamp_filename
from income_streams.common.config_loader import get_output_dir


class ProductDescriptionEngine:
    """AI engine for e-commerce product content."""

    def __init__(self):
        self.client = AIClient()

    def generate_product_listing(
        self,
        product_name: str,
        category: str = "",
        features: str = "",
        target_audience: str = "",
        platform: str = "salla",
        language: str = "ar",
    ) -> str:
        """Generate complete product listing content.

        Returns title, description, bullet points, SEO meta, and more.
        """
        lang = "Arabic" if language == "ar" else "English"
        platform_names = {"salla": "سلة", "zid": "زد", "shopify": "Shopify", "amazon": "Amazon"}

        system = f"""أنت خبير كتابة محتوى متاجر إلكترونية ومتخصص في {platform_names.get(platform, platform)}.
تكتب بـ{lang} وتعرف كيف تقنع المشتري بالشراء.

قواعدك:
- استخدم لغة تحفيزية (محدود، حصري، الأفضل مبيعاً)
- أبرز الفوائد قبل المميزات
- استخدم كلمات مفتاحية للسيو
- ناسب أسلوبك مع المنصة
- اكتب لجمهور السعودية والخليج"""

        prompt = f"""اكتب محتوى منتج كامل:

المنتج: {product_name}
الفئة: {category or 'عام'}
المميزات: {features or 'غير محدد'}
الجمهور المستهدف: {target_audience or 'عام'}
المنصة: {platform_names.get(platform, platform)}

أريد:
1. **عنوان المنتج** (محسّن للسيو، جذاب)
2. **وصف قصير** (2-3 جمل تظهر في نتائج البحث)
3. **وصف تفصيلي** (3-4 فقرات تقنع المشتري)
4. **نقاط مميزة** (5-7 bullet points)
5. **الكلمات المفتاحية** (10-15 كلمة)
6. **عنوان SEO** (60 حرف)
7. **وصف SEO Meta** (155 حرف)
8. **اقتراحات تصوير** (كيف يُصوّر المنتج)
9. **أسئلة شائعة** (3-5 أسئلة وأجوبة)
10. **منتجات مقترحة للبيع المشترك** (Cross-sell)"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=3000)

    def generate_batch(self, products: list, **kwargs) -> list:
        """Generate listings for multiple products."""
        results = []
        for i, product in enumerate(products, 1):
            print(f"[{i}/{len(products)}] Generating: {product}...")
            content = self.generate_product_listing(product, **kwargs)
            results.append({"product": product, "content": content})
        return results

    def optimize_existing_listing(self, current_listing: str) -> str:
        """Optimize an existing product listing for better conversion."""
        system = "أنت خبير تحسين معدلات التحويل (CRO) للمتاجر الإلكترونية."

        prompt = f"""حسّن هذا الوصف المنتج:

{current_listing}

أعطني:
1. النسخة المحسّنة (كاملة)
2. ما تم تغييره ولماذا
3. كلمات مفتاحية مقترحة
4. نصائح إضافية لزيادة المبيعات"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_collection_description(self, collection_name: str, products_overview: str) -> str:
        """Generate collection/category page description."""
        system = "اكتب وصف تصنيف/مجموعة لمتجر إلكتروني. محسّن للسيو وجذاب."

        prompt = f"""اكتب وصف لمجموعة: {collection_name}
المنتجات: {products_overview}

أعطني:
1. عنوان المجموعة (SEO)
2. وصف المجموعة (200 كلمة)
3. Meta description
4. كلمات مفتاحية"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=1500)


def main():
    parser = argparse.ArgumentParser(description="E-commerce Product Engine - محرك المنتجات")
    parser.add_argument("--product", "-p", required=True, help="Product name")
    parser.add_argument("--category", "-c", default="", help="Category")
    parser.add_argument("--features", "-f", default="", help="Features")
    parser.add_argument("--platform", default="salla", choices=["salla", "zid", "shopify", "amazon"])
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--save", "-s", action="store_true")

    args = parser.parse_args()
    engine = ProductDescriptionEngine()

    result = engine.generate_product_listing(
        args.product, args.category, args.features,
        platform=args.platform, language=args.language,
    )

    if args.save:
        output_dir = get_output_dir("content")
        filename = timestamp_filename(f"product_{args.product}", "md")
        path = save_output(result, filename, str(output_dir))
        print(f"Saved to: {path}")
    else:
        print(result)


if __name__ == "__main__":
    main()
