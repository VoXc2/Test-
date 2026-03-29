"""CLI runner for all prompt frameworks.

Usage:
    python -m prompt_frameworks.runner --list
    python -m prompt_frameworks.runner --framework career_survival --input "career_description=مهندس برمجيات 5 سنوات"
    python -m prompt_frameworks.runner --framework deep_thinking --input "problem_statement=كيف أبدأ مشروع AI"
"""

import argparse
import sys

from . import FRAMEWORKS


def list_frameworks():
    """Print all available frameworks."""
    print("\n" + "=" * 60)
    print("  أطر العمل المتاحة | Available Frameworks")
    print("=" * 60)

    for key, cls in FRAMEWORKS.items():
        fw = cls()
        info = fw.info()
        print(f"\n  [{key}]")
        print(f"  EN: {info['description']}")
        print(f"  AR: {info['description_ar']}")
        print(f"  Inputs: {', '.join(info['required_inputs'])}")

    print("\n" + "=" * 60)
    print("  Usage: python -m prompt_frameworks.runner --framework <name> --input '<key>=<value>'")
    print("=" * 60 + "\n")


def run_framework(name: str, inputs: dict):
    """Run a specific framework with given inputs."""
    if name not in FRAMEWORKS:
        print(f"Error: Framework '{name}' not found.")
        print(f"Available: {', '.join(FRAMEWORKS.keys())}")
        sys.exit(1)

    fw = FRAMEWORKS[name]()
    info = fw.info()

    print(f"\n{'=' * 60}")
    print(f"  Running: {info['name_ar']} | {info['name']}")
    print(f"{'=' * 60}\n")

    try:
        result = fw.run(**inputs)
        print(result)
        print(f"\n{'=' * 60}\n")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def parse_inputs(input_strings: list) -> dict:
    """Parse 'key=value' input strings into a dict."""
    inputs = {}
    for s in input_strings:
        if "=" not in s:
            print(f"Error: Input must be in 'key=value' format. Got: {s}")
            sys.exit(1)
        key, value = s.split("=", 1)
        inputs[key.strip()] = value.strip()
    return inputs


def main():
    parser = argparse.ArgumentParser(
        description="AI Prompt Frameworks Runner - أداة تشغيل أطر العمل"
    )
    parser.add_argument("--list", action="store_true", help="List all frameworks")
    parser.add_argument("--framework", "-f", type=str, help="Framework name to run")
    parser.add_argument("--input", "-i", type=str, action="append", default=[],
                        help="Input in 'key=value' format (can repeat)")

    args = parser.parse_args()

    if args.list:
        list_frameworks()
    elif args.framework:
        inputs = parse_inputs(args.input)
        run_framework(args.framework, inputs)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
