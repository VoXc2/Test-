"""AI Grammar Checker Tool."""

from income_streams.common import AIClient


class GrammarChecker:
    def __init__(self):
        self.client = AIClient()

    def check(self, text: str, language: str = "auto") -> str:
        system = """You are an expert proofreader and grammar checker.
For each issue found, show: the error, the correction, and a brief explanation.
Then provide the fully corrected text at the end."""

        prompt = f"""Check the following text for grammar, spelling, punctuation, and style issues.
Language: {language if language != 'auto' else 'auto-detect'}

Text:
{text}

Format your response as:
## Issues Found
1. [error] → [correction] - [explanation]
...

## Corrected Text
[full corrected text]"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=2000)
