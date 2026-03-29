"""Batch Translation Service.

Translate multiple files or large documents in chunks.

Usage:
    python -m income_streams.translation_service.batch_translator --dir ./docs --from en --to ar
"""

import argparse
import os
from pathlib import Path

from .translator import Translator
from income_streams.common.config_loader import get_output_dir


class BatchTranslator:
    """Translate multiple files or large documents."""

    def __init__(self):
        self.translator = Translator()

    def translate_directory(
        self,
        input_dir: str,
        source_lang: str = "en",
        target_lang: str = "ar",
        extensions: list = None,
        domain: str = "general",
    ) -> list:
        """Translate all matching files in a directory.

        Args:
            input_dir: Directory containing files to translate
            source_lang: Source language
            target_lang: Target language
            extensions: File extensions to process (default: .txt, .md)
            domain: Subject domain

        Returns:
            List of dicts with source/output paths
        """
        if extensions is None:
            extensions = [".txt", ".md", ".srt"]

        input_path = Path(input_dir)
        results = []

        files = [f for f in input_path.iterdir() if f.is_file() and f.suffix in extensions]

        print(f"\nFound {len(files)} files to translate")
        print(f"Direction: {source_lang} -> {target_lang}")
        print(f"Domain: {domain}\n")

        for i, file in enumerate(sorted(files), 1):
            print(f"[{i}/{len(files)}] Translating: {file.name}...", end=" ")
            try:
                output_path = self.translator.translate_file(
                    str(file),
                    source_lang=source_lang,
                    target_lang=target_lang,
                    domain=domain,
                )
                results.append({"source": str(file), "output": output_path, "status": "success"})
                print("Done")
            except Exception as e:
                results.append({"source": str(file), "output": None, "status": f"error: {e}"})
                print(f"Error: {e}")

        print(f"\nCompleted: {sum(1 for r in results if r['status'] == 'success')}/{len(results)} files")
        return results

    def translate_large_text(
        self,
        text: str,
        chunk_size: int = 2000,
        **kwargs,
    ) -> str:
        """Translate large text by splitting into chunks.

        Args:
            text: Large text to translate
            chunk_size: Max characters per chunk
            **kwargs: Passed to translator.translate()

        Returns:
            Full translated text
        """
        # Split by paragraphs to preserve context
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) > chunk_size and current_chunk:
                chunks.append(current_chunk)
                current_chunk = para
            else:
                current_chunk = current_chunk + "\n\n" + para if current_chunk else para

        if current_chunk:
            chunks.append(current_chunk)

        print(f"Split into {len(chunks)} chunks")
        translated_chunks = []

        for i, chunk in enumerate(chunks, 1):
            print(f"  Translating chunk {i}/{len(chunks)}...")
            translated = self.translator.translate(chunk, **kwargs)
            translated_chunks.append(translated)

        return "\n\n".join(translated_chunks)


def main():
    parser = argparse.ArgumentParser(description="Batch Translator - مترجم الدفعات")
    parser.add_argument("--dir", "-d", required=True, help="Directory with files to translate")
    parser.add_argument("--from", dest="source", default="en", help="Source language")
    parser.add_argument("--to", dest="target", default="ar", help="Target language")
    parser.add_argument("--domain", default="general")
    parser.add_argument("--ext", nargs="+", default=[".txt", ".md"], help="File extensions")

    args = parser.parse_args()
    batch = BatchTranslator()
    batch.translate_directory(args.dir, args.source, args.target, args.ext, args.domain)


if __name__ == "__main__":
    main()
