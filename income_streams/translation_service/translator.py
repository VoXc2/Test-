"""AI-Powered Context-Aware Translator - Income Stream #2.

Smart translation that understands context, not just words.
Supports glossary/terminology enforcement for specialized domains.

Usage:
    python -m income_streams.translation_service.translator --text "Hello world" --to ar
    python -m income_streams.translation_service.translator --file input.txt --from en --to ar
"""

import argparse
from pathlib import Path

import yaml

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config, get_output_dir, PROJECT_ROOT
from income_streams.common.utils import save_output, timestamp_filename


class Translator:
    """Context-aware AI translator with glossary support."""

    def __init__(self):
        self.client = AIClient(module_name="translation_service")
        self.config = get_config("translation_service")
        self.glossary = self._load_glossary()

    def _load_glossary(self) -> dict:
        """Load terminology glossary if available."""
        glossary_path = PROJECT_ROOT / self.config.get("glossary_path", "config/glossary.yaml")
        if glossary_path.exists():
            with open(glossary_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        return {}

    def translate(
        self,
        text: str,
        source_lang: str = "en",
        target_lang: str = "ar",
        domain: str = "general",
        preserve_formatting: bool = True,
    ) -> str:
        """Translate text with context awareness.

        Args:
            text: Text to translate
            source_lang: Source language code
            target_lang: Target language code
            domain: Subject domain (general, technical, medical, legal, business)
            preserve_formatting: Keep original formatting (markdown, etc.)

        Returns:
            Translated text
        """
        lang_names = {
            "ar": "Arabic", "en": "English", "fr": "French",
            "es": "Spanish", "de": "German", "tr": "Turkish",
        }
        source = lang_names.get(source_lang, source_lang)
        target = lang_names.get(target_lang, target_lang)

        # Build glossary context
        glossary_context = ""
        if self.glossary and domain in self.glossary:
            terms = self.glossary[domain]
            glossary_context = "\n\nUse these exact translations for domain terms:\n"
            for term, translation in terms.items():
                glossary_context += f"- {term} -> {translation}\n"

        system_prompt = f"""You are an expert {source}-to-{target} translator specializing in {domain} content.

Rules:
- Translate meaning and intent, not word-by-word
- Maintain the original tone and style
- Use natural, fluent {target} (not translationese)
- Keep proper nouns, brand names, and technical terms as appropriate
- {"Preserve all markdown/HTML formatting" if preserve_formatting else "Output plain text only"}
- For Arabic: use Modern Standard Arabic unless the context suggests a specific dialect
- Never add explanations or notes - output ONLY the translation
{glossary_context}"""

        prompt = f"Translate the following text from {source} to {target}:\n\n{text}"

        return self.client.generate(prompt, system_prompt=system_prompt, temperature=0.3)

    def translate_file(self, file_path: str, **kwargs) -> str:
        """Translate a text file and save the result."""
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        translated = self.translate(text, **kwargs)

        output_dir = get_output_dir("translations")
        source_name = Path(file_path).stem
        target_lang = kwargs.get("target_lang", "ar")
        filename = f"{source_name}_{target_lang}.md"
        return save_output(translated, filename, str(output_dir))


def main():
    parser = argparse.ArgumentParser(description="AI Translator - مترجم ذكي")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", "-t", help="Text to translate")
    group.add_argument("--file", "-f", help="File to translate")
    parser.add_argument("--from", dest="source", default="en", help="Source language (default: en)")
    parser.add_argument("--to", dest="target", default="ar", help="Target language (default: ar)")
    parser.add_argument("--domain", "-d", default="general",
                        choices=["general", "technical", "medical", "legal", "business"])
    parser.add_argument("--save", "-s", action="store_true", help="Save to file")

    args = parser.parse_args()
    translator = Translator()

    if args.file:
        path = translator.translate_file(args.file, source_lang=args.source, target_lang=args.target, domain=args.domain)
        print(f"\nTranslated file saved to: {path}")
    elif args.save:
        result = translator.translate(args.text, source_lang=args.source, target_lang=args.target, domain=args.domain)
        output_dir = get_output_dir("translations")
        filename = timestamp_filename("translation", "md")
        path = save_output(result, filename, str(output_dir))
        print(f"\nSaved to: {path}")
    else:
        result = translator.translate(args.text, source_lang=args.source, target_lang=args.target, domain=args.domain)
        print(result)


if __name__ == "__main__":
    main()
