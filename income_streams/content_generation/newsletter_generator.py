"""AI Newsletter Generator.

Creates engaging email newsletters with subject lines, previews, and content.

Usage:
    python -m income_streams.content_generation.newsletter_generator --topic "AI weekly digest" --name "AI Insider"
"""

import argparse
from pathlib import Path

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import read_template, format_template, timestamp_filename, save_output


class NewsletterGenerator:
    """Generate email newsletters using AI."""

    def __init__(self):
        self.client = AIClient(module_name="content_generation")
        self.template_dir = Path(__file__).parent / "templates"

    def generate(
        self,
        topic: str,
        newsletter_name: str = "AI Newsletter",
        language: str = "ar",
        tone: str = "informative",
    ) -> str:
        """Generate a complete newsletter.

        Args:
            topic: Newsletter theme/topic
            newsletter_name: Name of the newsletter
            language: 'ar' or 'en'
            tone: Writing tone

        Returns:
            Complete newsletter content
        """
        template = read_template(str(self.template_dir / "newsletter.txt"))
        prompt = format_template(
            template,
            topic=topic,
            newsletter_name=newsletter_name,
            language="Arabic" if language == "ar" else "English",
            tone=tone,
        )

        return self.client.generate(prompt, max_tokens=2500)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        """Generate and save to file."""
        content = self.generate(topic, **kwargs)
        output_dir = get_output_dir("content")
        filename = timestamp_filename(f"newsletter_{topic}", "md")
        return save_output(content, filename, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="Newsletter Generator - مولد النشرات البريدية")
    parser.add_argument("--topic", "-t", required=True, help="Newsletter topic")
    parser.add_argument("--name", "-n", default="AI Newsletter", help="Newsletter name")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"])
    parser.add_argument("--save", "-s", action="store_true", help="Save to file")

    args = parser.parse_args()
    gen = NewsletterGenerator()

    if args.save:
        path = gen.generate_and_save(args.topic, newsletter_name=args.name, language=args.language)
        print(f"\nSaved to: {path}")
    else:
        result = gen.generate(args.topic, newsletter_name=args.name, language=args.language)
        print(result)


if __name__ == "__main__":
    main()
