"""AI Email Writer Tool."""

from income_streams.common import AIClient


class EmailWriter:
    def __init__(self):
        self.client = AIClient()

    def write(
        self,
        purpose: str,
        recipient: str = "",
        tone: str = "professional",
        language: str = "ar",
        context: str = "",
    ) -> str:
        lang = "Arabic" if language == "ar" else "English"

        system = f"""You are an expert email writer. Write clear, effective emails in {lang}.
Output the email with Subject and Body. No explanations."""

        prompt = f"""Write a {tone} email.

Purpose: {purpose}
Recipient: {recipient or 'Not specified'}
Additional context: {context or 'None'}
Language: {lang}

Format:
Subject: [subject line]

[email body]"""

        return self.client.generate(prompt, system_prompt=system, max_tokens=1000)
