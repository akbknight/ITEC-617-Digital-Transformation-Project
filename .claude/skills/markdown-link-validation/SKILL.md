# Markdown Link Validation Skill

Use this skill to validate internal markdown links after moving or renaming files.

## When to use

- After reorganizing folders/files
- Before sharing instructor or student documentation
- During release/readiness checks

## Command

From repository root, run:

```bash
uv run scripts/validate_markdown_links.py \
  --root . \
  --report instructor-docs/ai-experiment/LINK-VALIDATION-REPORT.md \
  --title "Internal Markdown Link Validation Report"
```

## How to interpret

- Exit code `0`: all internal local links resolved.
- Exit code `1`: one or more broken links found.
- Console output shows `source-file:line -> target` for each failure.
- The report file contains summary metrics and issue list.

## Fix workflow

1. Update broken targets in the source markdown files.
2. Re-run the command.
3. Confirm zero broken links and keep the report with the test run.
