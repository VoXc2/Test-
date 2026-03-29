"""AI Text Summarizer Tool."""

from income_streams.common import AIClient


class TextSummarizer:
    def __init__(self):
        self.client = AIClient()

    def summarize(self, text: str, length: str = "medium", language: str = "auto") -> str:
        length_map = {
            "short": "2-3 sentences",
            "medium": "1 paragraph (5-7 sentences)",
            "long": "2-3 paragraphs with key points",
        }

        system = """You are an expert text summarizer. Create clear, accurate summaries
that capture the main ideas and key details. Maintain the original language unless asked otherwise.
Output ONLY the summary, no explanations."""

        prompt = f"""Summarize the following text in {length_map.get(length, length)}.
Language: {language if language != 'auto' else 'same as input'}

Text:
{text}"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=1000)
