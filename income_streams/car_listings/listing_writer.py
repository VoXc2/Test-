"""AI Car Listing Writer - Professional vehicle descriptions.
Usage: python -m income_streams.car_listings.listing_writer --make "تويوتا" --model "كامري" --year 2024
"""
import argparse
from income_streams.common import AIClient
from income_streams.common.config_loader import get_output_dir
from income_streams.common.utils import save_output, timestamp_filename

class CarListingWriter:
    def __init__(self):
        self.client = AIClient()

    def generate(self, make, model, year, condition="used", features="", price=0, language="ar"):
        lang = "Arabic" if language == "ar" else "English"
        system = (
            f"خبير تسويق سيارات ومحترف كتابة إعلانات معارض بـ{lang}. "
            "تكتب أوصاف تبيع السيارة بسرعة. تعرف السوق السعودي وتفضيلات المشترين."
        )
        price_text = f"السعر: {price} ريال" if price else "السعر: غير محدد (اقترح سعر مناسب)"
        prompt = f"""اكتب إعلان سيارة احترافي:
الشركة: {make}
الموديل: {model}
السنة: {year}
الحالة: {condition}
{"المميزات: " + features if features else ""}
{price_text}

أريد:
1. العنوان الإعلاني (جذاب وقصير)
2. الوصف التفصيلي (3-4 فقرات مقنعة)
3. المميزات الرئيسية (bullet points)
4. حالة السيارة
5. {"السعر المقترح (مع تبرير)" if not price else "تبرير السعر"}
6. نصائح التصوير (5 زوايا أساسية)
7. كلمات مفتاحية للبحث (حراج، موتري، إلخ)"""
        return self.client.generate(prompt, system_prompt=system, max_tokens=2500)

    def generate_and_save(self, make, model, year, **kw):
        content = self.generate(make, model, year, **kw)
        return save_output(content, timestamp_filename(f"car_{make}_{model}", "md"), str(get_output_dir("content")))

def main():
    parser = argparse.ArgumentParser(description="Car Listing Writer - كاتب إعلانات سيارات")
    parser.add_argument("--make", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--year", required=True)
    parser.add_argument("--condition", default="used", choices=["new", "used", "certified"])
    parser.add_argument("--features", "-f", default="")
    parser.add_argument("--price", type=float, default=0)
    parser.add_argument("--save", "-s", action="store_true")
    args = parser.parse_args()
    writer = CarListingWriter()
    if args.save:
        print(f"Saved to: {writer.generate_and_save(args.make, args.model, args.year, condition=args.condition, features=args.features, price=args.price)}")
    else:
        print(writer.generate(args.make, args.model, args.year, args.condition, args.features, args.price))

if __name__ == "__main__":
    main()
