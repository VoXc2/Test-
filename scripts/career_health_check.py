from pathlib import Path

required = [
    'README.md',
    'resume/CV_DATA.yaml',
    'resume/RESUME_EN.md',
    'resume/RESUME_AR.md',
    'portfolio/PROJECT_CASE_STUDIES.md',
    'career/TARGET_ROLES.md',
    'career/APPLICATION_PIPELINE.csv',
    'networking/LINKEDIN_PROFILE.md',
    'prompts/CAREER_AI_PROMPTS.md',
]

root = Path(__file__).resolve().parents[1]
missing = [p for p in required if not (root / p).exists()]

print('Career repo check')
print('missing:', missing)
raise SystemExit(1 if missing else 0)
