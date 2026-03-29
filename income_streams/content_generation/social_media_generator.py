"""AI Social Media Content Generator.

Generates platform-specific posts for Twitter/X, LinkedIn, Instagram.
Use to offer social media management services.

Usage:
    python -m income_streams.content_generation.social_media_generator --topic "tips for productivity" --platform twitter
    python -m income_streams.content_generation.social_media_generator --topic "نصائح ريادة الأعمال" --platform linkedin --language ar
"""

import argparse
from pathlib import Path

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import read_template, format_template, timestamp_filename, save_output


class SocialMediaGenerator:
    """Generate social media content for multiple platforms."""

    def __init__(self):
        self.client = AIClient(module_name="content_generation")
        self.config = get_config("content_generation")
        self.template_dir = Path(__file__).parent / "templates"

    def generate(
        self,
        topic: str,
        platform: str = "twitter",
        language: str = "ar",
        tone: str = "engaging",
        count: int = 3,
    ) -> str:
        """Generate social media posts.

        Args:
            topic: Content topic
            platform: twitter, linkedin, or instagram
            language: 'ar' or 'en'
            tone: Writing tone
            count: Number of post variations

        Returns:
            Generated posts as formatted string
        """
        template = read_template(str(self.template_dir / "social_post.txt"))
        prompt = format_template(
            template,
            topic=topic,
            platform=platform.capitalize(),
            language="Arabic" if language == "ar" else "English",
            tone=tone,
            count=str(count),
        )

        return self.client.generate(prompt, max_tokens=2000)

    def generate_all_platforms(self, topic: str, language: str = "ar") -> dict:
        """Generate posts for all platforms at once."""
        results = {}
        for platform in ["twitter", "linkedin", "instagram"]:
            results[platform] = self.generate(topic, platform=platform, language=language)
        return results

    def generate_and_save(self, topic: str, **kwargs) -> str:
        """Generate and save to file."""
        content = self.generate(topic, **kwargs)
        output_dir = get_output_dir("content")
        platform = kwargs.get("platform", "social")
        filename = timestamp_filename(f"{platform}_{topic}", "md")
        return save_output(content, filename, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="Social Media Content Generator - مولد محتوى السوشال")
    parser.add_argument("--topic", "-t", required=True, help="Content topic")
    parser.add_argument("--platform", "-p", default="twitter",
                        choices=["twitter", "linkedin", "instagram", "all"], help="Platform")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--count", "-c", type=int, default=3, help="Number of variations")
    parser.add_argument("--save", "-s", action="store_true", help="Save to file")

    args = parser.parse_args()
    gen = SocialMediaGenerator()

    if args.platform == "all":
        results = gen.generate_all_platforms(args.topic, language=args.language)
        for platform, content in results.items():
            print(f"\n{'='*40} {platform.upper()} {'='*40}")
            print(content)
    elif args.save:
        path = gen.generate_and_save(args.topic, platform=args.platform, language=args.language, count=args.count)
        print(f"\nSaved to: {path}")
    else:
        result = gen.generate(args.topic, platform=args.platform, language=args.language, count=args.count)
        print(result)


if __name__ == "__main__":
    main()
