# Changelog

All notable changes to the Enterprise IT Navigator Simulation are documented here.

## [1.0.2] - 2026-02-24

### Changed

- **CI Workflow: Add Pytest Step**
  - Renamed workflow from "Markdown Link Validation" to "Tests & Link Validation"
  - Pytest runs before link validation on every push to `main` and all PRs
  - Tests must pass before link validation proceeds

## [1.0.1] - 2026-02-24

### Added

- **Pytest Suite for Markdown Link Validator**
  - `tests/test_validate_markdown_links.py` — 42 tests covering all public functions
  - Test classes: `TestParseMarkdownLinks` (10), `TestIsLocalTarget` (9), `TestResolveTarget` (7), `TestDiscoverMarkdownFiles` (4), `TestCollectBrokenLinks` (7), `TestGenerateReportMarkdown` (2), `TestMainCLI` (3)
  - CLI integration tests verify exit codes 0/1 and `--report` flag file output

## [1.0.0] - 2026-02-24

### Added

- **Markdown Link Integrity Automation**
  - `scripts/validate_markdown_links.py` — PEP 723 script that discovers all `.md` files, parses internal markdown links, resolves relative paths, and reports broken links with source file, line number, and target
  - `.claude/skills/markdown-link-validation/SKILL.md` — Claude Code skill documenting usage, interpretation, and fix workflow
  - `.github/workflows/markdown-link-validation.yml` — CI workflow runs on push to `main` and all PRs; uploads report artifact with 30-day retention
  - `.vscode/tasks.json` — VS Code task "Validate Markdown Links" (tracked via `.gitignore` carve-out `!.vscode/tasks.json`)

- **Presentation-Day Support Templates**
  - `student-workspace/source-docs/presentation-support/` — new folder for AI-generated defense materials
  - `presentation-support/README.md` — index explaining folder purpose and file listing
  - `presentation-support/industry-judge-analysis-and-qna.md` — blank template with rubric-aligned sections for judge analysis, likely questions by persona, 30-second response patterns, and scale-gate thresholds
  - `presentation-support/day-of-defense-cheat-sheet.md` — blank template for one-page defense script with opening pitch, key numbers, core argument, top Q&A responses, scale-gate criteria, verbal guardrails, and closing statement
  - `presentation-support/day-of-defense-cheat-sheet-compact.md` — condensed single-card version
  - `presentation-support/day-of-defense-speaker-split.md` — blank template for speaker allocations, individual notes, interruption handling, hand-off lines, Q&A assignment matrix, and pre-presentation huddle

- **Instructor AI Experiment Bundle** (excluded from student template via `.gitignore`)
  - `instructor-docs/ai-experiment/README.md` — index of all instructor evaluation artifacts with operations guide
  - `instructor-docs/ai-experiment/INSTRUCTOR-AI-EXPERIMENT-INSIGHTS.md` — detailed findings from end-to-end test run
  - `instructor-docs/ai-experiment/INSTRUCTOR-AI-EXPERIMENT-HANDOUT.md` — concise shareable faculty summary
  - `instructor-docs/ai-experiment/LESSONS_LEARNED_RECOMMENDED_IMPROVEMENTS.md` — session observations and prioritized improvement backlog
  - `instructor-docs/ai-experiment/AI-TEST-METRICS-TEMPLATE.md` — reusable 13-section measurement template for future AI experiments
  - `instructor-docs/ai-experiment/CHAT-CONTEXT-TRANSCRIPT-SUMMARY.md` — chronological session reconstruction
  - `instructor-docs/ai-experiment/LINK-VALIDATION-REPORT.md` — placeholder for link validation output

### Changed

- **`.gitignore` Updates**
  - Added `!.vscode/tasks.json` carve-out to track VS Code task definition while keeping other IDE settings ignored
  - Added `instructor-docs/` exclusion so instructor materials exist in the original repo but do not ship to student template copies

- **Student Documentation Cross-Links**
  - `README.md` — added "Markdown Link Check" section documenting VS Code task, CLI command, and CI automation; updated repository structure tree with `presentation-support/` and `scripts/`
  - `QUICKSTART-CLAUDE-CODE.md` — added "Link Validation" section with `/markdown-link-validation` skill reference
  - `QUICKSTART-COPILOT.md` — added "Link Validation" section with VS Code task instructions
  - `STUDENT-GUIDE.md` — added `presentation-support/` folder reference in workflow step 8; added link validation tip
  - `student-workspace/source-docs/README.md` — added "Presentation-Day Support" section pointing to `presentation-support/`

### Changed

- **Convert to GitHub Template Repository**
  - Replaced `git clone` instructions with "Use this template" workflow in all 4 student-facing docs (README.md, QUICKSTART-CLAUDE-CODE.md, QUICKSTART-COPILOT.md, STUDENT-GUIDE.md)
  - Each student team now creates their own private repo from the template, getting a clean git history
  - Teams cannot push back to the original repo — they file issues if they find problems
  - Requires enabling "Template repository" in GitHub repo Settings

### Fixed

- **PEP 723 Inline Script Metadata for `extract_presentation.py`**
  - Added `# /// script` metadata block with `requires-python` and `python-pptx` dependency
  - Students can now run `uv run extract_presentation.py` without `pyproject.toml` (which is excluded from the public repo)
  - Simplified command: `uv run extract_presentation.py` (no `python` argument needed)
  - Updated all 20 remaining references (`uv run python extract_presentation.py` → `uv run extract_presentation.py`) across 9 skills, 9 agents, `CLAUDE-student.md`, and `README.md`

### Changed

- **Student Documentation Accessibility Overhaul**
  - `README-student.md`: Added "What You Need" prerequisites table, reordered Getting Started (install → clone → choose AI → brief), added Python/uv install section with links, added troubleshooting table
  - `QUICKSTART-COPILOT.md`: Expanded prerequisites with install verification commands and links, added "Don't have Git?" callout, marked Step 8 as optional, added Python/uv install instructions, added troubleshooting table
  - `QUICKSTART-CLAUDE-CODE.md`: Same prerequisite improvements, noted Claude Code can read `.pptx`/`.pdf` directly (extraction optional), added Python/uv install instructions, added troubleshooting table
  - `STUDENT-GUIDE.md`: Broke dense workflow step 1 into sub-bullets for readability, added Python/uv install links and Claude Code alternative in step 7, added Git install link in "Two Ways to Use" section
  - `.gitignore`: Added patterns for student-uploaded assignment deliverables in `source-docs/` (`.pdf`, `.docx`, `.xlsx`, `.txt`)

### Added

- **Milestone-Aware `/setup-project` Enhancement**
  - Rewrote `/setup-project` skill and Copilot prompt from 6-phase to 8-phase milestone-aware flow
  - Phase 1: Scan & Detect — reads project brief, scans `student-workspace/source-docs/` for prior deliverables, checks ROI/OCM companion files and extracted presentation
  - Phase 2: Milestone Identification — infers assignment stage (1-7) from evidence, asks student to confirm
  - Phase 3: Welcome & Milestone-Adapted Status — tailored welcome and scope for each stage
  - Phase 4: Interactive Q&A (Milestone-Filtered) — same 10 sections, prioritized by milestone; includes assignment-specific guidance baked into skill text (approved industries for Assignment 2, technology categories for Assignment 3, cost/benefit categories for Assignment 5, Rogers' 5 factors for Assignment 6)
  - Phase 5: Write the Brief — also writes `roi-summary.md` and `ocm-assessment.md` when discussed in depth
  - Phase 6: Quality Review (Milestone-Calibrated) — expectations calibrated to student's current stage
  - Phase 7: Milestone-Specific Next Steps (NEW) — maps to next assignment with specific requirements and persona recommendations
  - Phase 8: Wrap-Up — summary, roadmap, and persona consultation recommendations tuned to milestone

- **Companion Templates**
  - `student-workspace/roi-summary.md` — structured ROI template: cost/benefit categories (technology, implementation, training, operations), key metrics (ROI, payback, NPV), assumptions checklist, sensitivity analysis table, sources/benchmarks
  - `student-workspace/ocm-assessment.md` — Rogers' 5-factor assessment template: Relative Advantage, Trialability, Compatibility, Observability, Complexity with Yes/No/Mixed ratings, mitigations, stakeholder impact table, communication plan, resistance assessment

- **Source Documents Directory**
  - `student-workspace/source-docs/` — students drop prior assignment deliverables (PDFs, DOCXs) here for AI context
  - `student-workspace/source-docs/README.md` — explains what to put here and supported file types

- **Companion File Awareness Across Personas**
  - CFO skill and agent now read `roi-summary.md` before responding
  - CHRO skill and agent now read `ocm-assessment.md` before responding
  - Evaluate skill and prompt now read both companion files to inform Financial Analysis and Change Management scoring

### Changed

- **Interactive Project Brief Setup (`/setup-project`)**
  - Upgraded from 6-phase generic flow to 8-phase milestone-aware flow
  - Setup now detects which assignment the student is working on and adapts Q&A accordingly
  - Assignment-specific guidance from course requirements baked into skill text (not requiring access to Group-Assignments/ directory)
  - Students at early milestones get focused guidance without being overwhelmed by advanced expectations

- **Documentation Updates**
  - Updated STUDENT-GUIDE.md workflow step 1 with source-docs and milestone awareness
  - Updated QUICKSTART-COPILOT.md and QUICKSTART-CLAUDE-CODE.md Step 4 with source-docs, milestone detection, and companion templates
  - Updated README-student.md repo structure with new files and getting started instructions
  - Updated CLAUDE-student.md workflow with source-docs and companion template references
  - Updated `.github/copilot-instructions.md` with source-docs and companion template descriptions

---

- **Interactive Project Brief Setup (`/setup-project`)** *(initial version)*
  - New Claude Code skill `.claude/skills/setup-project/SKILL.md` — 6-phase interactive Q&A flow
  - New Copilot prompt `.github/prompts/setup-project.prompt.md` — same flow with `mode: "agent"` for file write access
  - Walks students through each project brief section one at a time conversationally
  - Assesses existing brief state (complete/partial/empty) and adapts accordingly
  - Writes the completed brief preserving exact template structure
  - Reviews for quality: flags vague sections, remaining placeholders, and thin answers
  - Follow-ups framed from executive perspectives ("The CFO will ask about this...")
  - Updated all student-facing docs: quickstart guides (Option A/B pattern), STUDENT-GUIDE.md, README-student.md, CLAUDE-student.md
  - Added `setup-project` to `.github/copilot-instructions.md` prompt references


- **Public Student Repo and Sync System**
  - Created public repo `ITEC-617-Digital-Transformation-Project-Coach` for students to clone
  - `sync-to-student-repo.sh` — whitelist-based sync script copies only student-facing content
  - `README-student.md` — tailored README for the public repo (becomes `README.md` on sync)
  - `CLAUDE-student.md` — tailored Claude Code context for students (becomes `CLAUDE.md` on sync)
  - Public repo contains: primer/, rubrics/, student-workspace/, .github/agents+prompts, .claude/skills/, quickstart guides, extract_presentation.py
  - Private content stays private: src/, tests/, docs/, syllabus, API config, instructor materials

- **Evaluation Progress Tracking (Upgrade 1)**
  - Students can now evaluate multiple times and see score improvement over time
  - Session state tracks evaluation history with timestamps and engaged personas
  - `compute_evaluation_delta()` computes per-dimension score changes between evaluations
  - `generate_progress_report()` produces a markdown progress report
  - Evaluation dashboard shows metric cards with delta arrows for each run
  - First-to-latest dimension delta table appears after 2+ evaluations
  - "Export Progress Report" button writes to `student-workspace/extracted/progress-report.md`
  - New unit tests in `TestEvaluationHistory` covering delta computation and report generation

- **Industry Judge Advice Integration (Upgrade 3)**
  - New primer section `primer/16-judge-advice.md` consolidating 4 years of judge feedback (2021-2024)
  - 10 recurring themes with actionable advice and memorable judge quotes
  - New `judge_advice` entry in `PRIMER_SECTIONS` knowledge base
  - All 9 personas now include `judge_advice` in their `primer_topics` for automatic context injection
  - System prompt template includes judge coaching directive
  - Judge Coaching Context sections added to all 9 GitHub Copilot agent files (`.github/agents/*.agent.md`)
  - Judge Coaching Context sections added to all 9 Claude Code skill files (`.claude/skills/*/SKILL.md`)
  - Judge Perspective notes added to 5 rubric dimension files (business case, financial analysis, implementation strategy, change management, presentation readiness)
  - Updated knowledge base tests for 16 sections and judge advice validation

### Changed

- **Persona Diversity Update (Upgrade 2)**
  - Renamed Legal persona from "Marcus Thompson" to "Jonathan Shapiro" across all 10 files
  - No functional changes — persona ID (`legal`), role, and behavior remain identical
