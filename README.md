# Career Workspace

A clean workspace for managing CV material, portfolio evidence, job applications, LinkedIn content, outreach, and interview preparation.

## Main folders

- `profile/` — profile summaries and positioning
- `resume/` — CV drafts and structured data
- `portfolio/` — project case studies
- `career/` — target roles, keywords, and application tracker
- `networking/` — LinkedIn and outreach material
- `letters/` — cover letter templates
- `interview/` — interview preparation
- `prompts/` — reusable AI prompts
- `scripts/` — local checks and generators

## Commands

```bash
python scripts/career_health_check.py
python scripts/generate_resume_pack.py
```

## Workflow

1. Update `resume/CV_DATA.yaml`.
2. Add project evidence in `portfolio/PROJECT_CASE_STUDIES.md`.
3. Tailor each CV using `prompts/CAREER_AI_PROMPTS.md`.
4. Track opportunities in `career/APPLICATION_PIPELINE.csv`.
5. Run the health check before submitting applications.
