"""AI Blog Post Generator - Income Stream #1.

Generates SEO-optimized blog posts in Arabic and English.
Use this to offer content writing services on Khamsat/Fiverr/Upwork.

Usage:
    python -m income_streams.content_generation.blog_generator --topic "الذكاء الاصطناعي في التعليم" --language ar
    python -m income_streams.content_generation.blog_generator --topic "AI in healthcare" --language en --tone casual
"""

import argparse
from pathlib import Path

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir
from income_streams.common.utils import read_template, format_template, timestamp_filename, save_output


class BlogGenerator:
    """Generate SEO-optimized blog posts using AI."""

    def __init__(self):
        self.client = AIClient(module_name="content_generation")
        self.config = get_config("content_generation")
        self.template_dir = Path(__file__).parent / "templates"

    def generate(
        self,
        topic: str,
        language: str = "ar",
        tone: str = "professional",
        word_count: int = 1200,
    ) -> str:
        """Generate a full blog post.

        Args:
            topic: The blog post topic/title
            language: 'ar' for Arabic, 'en' for English
            tone: Writing tone (professional, casual, academic, friendly)
            word_count: Target word count

        Returns:
            Complete blog post as formatted string
        """
        template = read_template(str(self.template_dir / "blog_post.txt"))
        prompt = format_template(
            template,
            topic=topic,
            language="Arabic" if language == "ar" else "English",
            tone=tone,
            word_count=str(word_count),
        )

        return self.client.generate(prompt, max_tokens=3000)

    def generate_and_save(self, topic: str, **kwargs) -> str:
        """Generate and save to file. Returns file path."""
        content = self.generate(topic, **kwargs)
        output_dir = get_output_dir("content")
        filename = timestamp_filename(topic, "md")
        return save_output(content, filename, str(output_dir))

    def generate_batch(self, topics: list, **kwargs) -> list:
        """Generate multiple blog posts for a list of topics."""
        results = []
        for topic in topics:
            path = self.generate_and_save(topic, **kwargs)
            results.append({"topic": topic, "path": path})
            print(f"  ✓ Generated: {topic} -> {path}")
        return results


def main():
    parser = argparse.ArgumentParser(description="AI Blog Post Generator - مولد المقالات")
    parser.add_argument("--topic", "-t", required=True, help="Blog post topic")
    parser.add_argument("--language", "-l", default="ar", choices=["ar", "en"], help="Language")
    parser.add_argument("--tone", default="professional", help="Tone: professional, casual, academic")
    parser.add_argument("--words", "-w", type=int, default=1200, help="Target word count")
    parser.add_argument("--save", "-s", action="store_true", help="Save to file")

    args = parser.parse_args()
    gen = BlogGenerator()

    if args.save:
        path = gen.generate_and_save(args.topic, language=args.language, tone=args.tone, word_count=args.words)
        print(f"\nSaved to: {path}")
    else:
        result = gen.generate(args.topic, language=args.language, tone=args.tone, word_count=args.words)
        print(result)


if __name__ == "__main__":
    main()
