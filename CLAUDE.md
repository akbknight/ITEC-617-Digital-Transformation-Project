# ITEC-617 Digital Transformation Project Coach

## Project Overview

This is an LLM-powered interactive simulation for MBA students in AU Kogod ITEC-617 (Information and Technology). It helps students prepare their Digital Transformation team project presentations by challenging them from multiple executive perspectives.

## How to Use

- **Project Setup**: Use `/setup-project` to interactively fill in your project brief through guided Q&A
- **Persona Skills**: Use `/cio`, `/cfo`, `/ciso`, `/coo`, `/chro`, `/cto`, `/cdo`, `/legal`, `/procurement` to consult executive personas
- **Evaluation**: Use `/evaluate` to score your proposal across 9 rubric dimensions (45 criteria)
- **Presentation Prep**: Use `/presentation-prep` for mock Q&A with a simulated judge panel

## Key Course Context

- **Course**: ITEC-617 Information and Technology (1.5 credits, MBA)
- **Project**: Teams present a business case for a pilot application of emerging technology to address a specific business need
- **Presentation**: 10 minutes + 2-3 minutes Q&A, presented to industry judges
- **Goal**: Persuade senior executive audience to invest in proposed pilot/proof-of-concept
- **DT Project Weight**: 50% of final grade
- **Presentation Date**: April 27, 2026 (Class 7 of 8)

## Grounding Sources

- **Enterprise IT Primer Website**: https://leifulstrup.github.io/enterprise-it-primer/
- **Course Catalog**: https://catalog.american.edu/preview_course_nopop.php?catoid=21&coid=101514

## Executive Personas (9)

| ID | Name | Title | Focus |
|----|------|-------|-------|
| cio | Jordan Chen | CIO | IT strategy, governance, enterprise architecture |
| ciso | Anika Patel | CISO | Cybersecurity, risk, privacy, compliance |
| cfo | Robert Okafor | CFO | Financial analysis, ROI, TCO, budget impact |
| coo | Maria Santos | COO | Operations, implementation, pilot design |
| chro | David Washington | CHRO | Change management, people, culture |
| cto | Priya Ramanathan | CTO | Technology, innovation, architecture |
| cdo | Sarah Kim | CDO | Data strategy, governance, AI ethics |
| legal | Jonathan Shapiro | General Counsel | Legal, regulatory, IP, compliance |
| procurement | Lisa Fernandez | VP Procurement | Vendor strategy, contracts, negotiation |

## Content Directories

- `primer/` - 16 reference sections: 15 Enterprise IT Primer + industry judge advice (markdown, for LLM context and student reference)
- `rubrics/` - 9 evaluation dimensions, 45 criteria (markdown, for scoring and feedback)
- `student-workspace/` - Project brief, presentation notes, ROI summary, OCM assessment templates
- `student-workspace/source-docs/` - Students drop prior assignment deliverables here for AI context

## Student Workflow

1. Drop any prior assignment deliverables (PDFs, DOCXs) into `student-workspace/source-docs/`, then run `/setup-project` to interactively fill in your project brief. The setup flow detects your current assignment milestone and adapts its questions accordingly. For ROI work, use `student-workspace/roi-summary.md`; for OCM, use `student-workspace/ocm-assessment.md`. Or manually edit `student-workspace/project-brief.md`.
2. Consult executive personas using slash commands (`/cio`, `/cfo`, etc.). The CFO also reads `roi-summary.md` and the CHRO also reads `ocm-assessment.md` when those files have content.
3. Run `/evaluate` after 3-4 persona consultations to see your scores (also considers ROI and OCM companion files)
4. Address gaps by consulting personas who cover your lowest-scoring dimensions
5. Once you have draft slides, place a **copy** of your `.pptx` in `student-workspace/slides/` and run:
   ```
   uv run extract_presentation.py
   ```
   Always keep your original PowerPoint in a separate folder. Use `git commit` to snapshot your work before each AI feedback session.
6. Run `/presentation-prep` for mock Q&A practice

## Student Documentation

- `STUDENT-GUIDE.md` - Overview of the simulation, personas, and how scoring works
- `QUICKSTART-CLAUDE-CODE.md` - Step-by-step setup and usage instructions
