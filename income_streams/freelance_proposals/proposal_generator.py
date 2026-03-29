"""AI Freelance Proposal Generator - Income Stream #4.

Takes a job posting and generates a winning, personalized proposal.
Use this to respond to freelance jobs faster and with higher win rates.

Usage:
    python -m income_streams.freelance_proposals.proposal_generator --job "Need a blog writer for tech content" --platform upwork
    python -m income_streams.freelance_proposals.proposal_generator --job "محتاج مصمم لوقو" --platform khamsat --skills "تصميم, فوتوشوب"
"""

import argparse
from pathlib import Path

from income_streams.common import AIClient
from income_streams.common.config_loader import get_config
from income_streams.common.utils import read_template, format_template


class ProposalGenerator:
    """Generate winning freelance proposals using AI."""

    def __init__(self):
        self.client = AIClient(module_name="freelance_proposals")
        self.config = get_config("freelance_proposals")
        self.template_dir = Path(__file__).parent / "templates"

    def generate(
        self,
        job_description: str,
        platform: str = "upwork",
        skills: str = "",
        experience: str = "",
        language: str = None,
        max_words: int = 300,
    ) -> str:
        """Generate a tailored proposal for a job posting.

        Args:
            job_description: The full job posting text
            platform: upwork, fiverr, khamsat, or mostaql
            skills: Your relevant skills (comma-separated)
            experience: Brief description of your experience
            language: Override language (auto-detects from platform)
            max_words: Maximum proposal length

        Returns:
            Complete proposal text ready to submit
        """
        if language is None:
            language = "Arabic" if platform in ("khamsat", "mostaql") else "English"
        else:
            language = "Arabic" if language == "ar" else "English"

        template = read_template(str(self.template_dir / "proposal_template.txt"))
        prompt = format_template(
            template,
            job_description=job_description,
            platform=platform.capitalize(),
            language=language,
            skills=skills or "Versatile professional with broad experience",
            experience=experience or "Multiple successful projects in this field",
            max_words=str(max_words),
        )

        return self.client.generate(prompt, max_tokens=1500)

    def generate_variations(self, job_description: str, count: int = 3, **kwargs) -> list:
        """Generate multiple proposal variations to choose from."""
        variations = []
        for i in range(count):
            proposal = self.generate(job_description, **kwargs)
            variations.append(proposal)
        return variations


def main():
    parser = argparse.ArgumentParser(description="Freelance Proposal Generator - مولد عروض الفريلانس")
    parser.add_argument("--job", "-j", required=True, help="Job description text")
    parser.add_argument("--platform", "-p", default="upwork",
                        choices=["upwork", "fiverr", "khamsat", "mostaql"])
    parser.add_argument("--skills", "-s", default="", help="Your skills (comma-separated)")
    parser.add_argument("--experience", "-e", default="", help="Your experience summary")
    parser.add_argument("--language", "-l", choices=["ar", "en"], help="Override language")
    parser.add_argument("--variations", "-v", type=int, default=1, help="Number of variations")

    args = parser.parse_args()
    gen = ProposalGenerator()

    if args.variations > 1:
        proposals = gen.generate_variations(
            args.job, count=args.variations, platform=args.platform,
            skills=args.skills, experience=args.experience, language=args.language,
        )
        for i, p in enumerate(proposals, 1):
            print(f"\n{'='*40} Variation {i} {'='*40}")
            print(p)
    else:
        result = gen.generate(
            args.job, platform=args.platform, skills=args.skills,
            experience=args.experience, language=args.language,
        )
        print(result)


if __name__ == "__main__":
    main()
