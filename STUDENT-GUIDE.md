# Enterprise IT Navigator - Student Guide

## What is the Enterprise IT Navigator?

The Enterprise IT Navigator is an AI-powered simulation that helps you prepare for your ITEC-617 Digital Transformation (DT) team project presentation. Rather than going into your presentation cold, you consult with 9 simulated executive personas who challenge your proposal from different C-suite perspectives, get scored on 9 rubric dimensions with 45 total criteria, and practice mock Q&A -- all before your real presentation to industry judges on April 27, 2026.

The simulation is grounded in the [Enterprise IT Primer](https://leifulstrup.github.io/enterprise-it-primer/), so the executives reference the same frameworks and concepts you are learning in ITEC-617.

## The Executive Personas

Each persona has a distinct personality, priorities, and communication style. They will ask probing questions, push back on vague answers, and provide constructive guidance.

| Persona | Name | Title | Focus Areas |
|---------|------|-------|-------------|
| CIO | Jordan Chen | Chief Information Officer | IT strategy, governance, enterprise architecture |
| CISO | Anika Patel | Chief Information Security Officer | Cybersecurity, risk, privacy, compliance |
| CFO | Robert Okafor | Chief Financial Officer | Financial analysis, ROI, TCO, budget impact |
| COO | Maria Santos | Chief Operating Officer | Operations, implementation, pilot design |
| CHRO | David Washington | Chief Human Resources Officer | Change management, people, culture |
| CTO | Priya Ramanathan | Chief Technology Officer | Technology, innovation, architecture |
| CDO | Sarah Kim | Chief Data Officer | Data strategy, governance, AI ethics |
| Legal | Jonathan Shapiro | General Counsel | Legal, regulatory, IP, compliance |
| Procurement | Lisa Fernandez | VP of Procurement | Vendor strategy, contracts, negotiation |

## How You're Evaluated

Your proposal is evaluated across 9 rubric dimensions. Each dimension contains multiple criteria, and each criterion is scored on a 1-5 scale.

### Rubric Dimensions and Weights

| # | Dimension | Weight | Key Personas |
|---|-----------|--------|--------------|
| 1 | Business Case Strength | 20% | CFO, COO |
| 2 | Technology Selection and Feasibility | 10% | CTO, CIO |
| 3 | Financial Analysis | 15% | CFO |
| 4 | Risk and Security Assessment | 10% | CISO, Legal |
| 5 | Implementation Strategy | 15% | COO, CIO, CTO |
| 6 | Change Management and People | 10% | CHRO, COO |
| 7 | Data and Analytics | 5% | CDO |
| 8 | Vendor and Sourcing Strategy | 5% | Procurement |
| 9 | Presentation Readiness | 10% | All |

### Scoring Scale

| Score | Label | Description |
|-------|-------|-------------|
| 1 | Not Addressed | Topic not mentioned or considered |
| 2 | Superficial | Acknowledged but lacks depth or evidence |
| 3 | Adequate | Reasonable treatment with some supporting evidence |
| 4 | Strong | Well-developed with evidence, frameworks, and analysis |
| 5 | Exceptional | Comprehensive, nuanced, with creative insights and strong evidence |

### Readiness Levels

Your composite weighted score maps to a readiness level:

| Score Range | Readiness Level | Meaning |
|-------------|----------------|---------|
| 90-100% | Ready to Present | Strong across all dimensions |
| 75-89% | Nearly Ready | Minor gaps to address |
| 60-74% | Making Progress | Several areas need deepening |
| 40-59% | Early Stage | Significant gaps in multiple areas |
| 0-39% | Needs Rethinking | Fundamental issues with the approach |

## Recommended Workflow

Follow this sequence to get the most out of the simulation:

1. **Fill in your project brief.**
   - Use `/setup-project` (Claude Code) or the **setup-project** prompt (Copilot) to walk through each section interactively.
   - The setup flow is **milestone-aware** — it detects where you are in the assignment sequence (Team Charter through Final Presentation), adapts its questions to your current stage, and provides guidance specific to your next assignment.
   - If you have completed prior assignments, drop copies of your deliverables (PDFs, DOCXs) into `student-workspace/source-docs/` before running setup — the AI will extract relevant context and skip questions you have already answered.
   - For ROI and OCM work, dedicated templates are available at `student-workspace/roi-summary.md` and `student-workspace/ocm-assessment.md`.
   - You can also open `student-workspace/project-brief.md` and complete sections manually. The more detail you provide, the better the executive feedback.

2. **Start the simulation.** Run the start simulation prompt to get an analysis of your project brief, an assessment of strengths and gaps, and a recommended sequence of executive personas to consult.

3. **Consult executive personas.** Begin with the three essential executives -- CIO, CFO, and CISO -- then follow the simulation's personalized recommendations. Each persona conversation works best when you come with specific questions and are prepared to defend your proposal.

4. **Evaluate your proposal.** After 3-4 persona consultations, run the evaluation prompt to see your scores across all 9 dimensions. This shows you exactly where you stand and where to focus next.

5. **Address gaps.** Based on your evaluation, consult the personas who cover your lowest-scoring dimensions. Update your project brief as your thinking evolves.

6. **Prepare your presentation.** Build your PowerPoint slides and fill in `student-workspace/presentation-notes.md` with your slide-by-slide notes and talking points.

7. **Extract your presentation for AI feedback.** Once you have a draft PowerPoint, place a **copy** of your `.pptx` file in `student-workspace/slides/` and run:
   ```
   uv run extract_presentation.py
   ```
   This extracts all slide text, speaker notes, and structure into a format the AI can analyze. For visual feedback on charts and layout, also export your presentation as PDF (File > Export > PDF) and save it in the same `student-workspace/slides/` folder.

   > **Claude Code users**: Claude Code can read `.pptx` and `.pdf` files directly — you can skip extraction and just ask Claude to review your slides.

   > **Don't have Python or uv?** Install Python 3.12+ from [python.org/downloads](https://www.python.org/downloads/) and uv from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/). This step is optional — the AI can still evaluate your project based on your brief without extracting slides.

   > **Protect your work.** Always keep your original PowerPoint in a separate folder outside this repository (e.g., your Desktop or OneDrive). AI tools can sometimes modify files in your workspace inadvertently. Make a habit of saving backup copies or using `git commit` to snapshot your work before each AI feedback session. That way you can always recover a previous version.

8. **Get slide-by-slide feedback.** Now when you consult personas or run evaluation, they will provide feedback on your *actual slides* — identifying which slides are strong, which need work, and what's missing from your presentation. AI-generated defense materials (judge Q&A, cheat sheets, speaker splits) land in `student-workspace/source-docs/presentation-support/`.

9. **Practice mock Q&A.** Run the presentation prep prompt, which simulates a panel of industry judges asking tough questions based on your actual slide content and weakest areas. This is the closest practice you will get to the real thing.

10. **Get next steps.** Run the next-steps prompt for a prioritized improvement plan with specific frameworks, primer references, and slide-level recommendations.

11. **Iterate.** Continue refining your slides and re-running extraction + evaluation until your readiness score reaches 75% or higher. Teams that reach "Nearly Ready" or above tend to perform well with industry judges.

## Two Ways to Use the Simulation

First, make sure you have **Git** installed ([git-scm.com/downloads](https://git-scm.com/downloads)), then create your team's copy of the simulation repo if you haven't already:

1. Go to [github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach](https://github.com/leifulstrup/ITEC-617-Digital-Transformation-Project-Coach).
2. Click the green **"Use this template"** button → **"Create a new repository"**.
3. Name your repo (e.g., `Team-Name-DT-Project`), set it to **Private**, and click **"Create repository"**.
4. Clone your new repo:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

The Enterprise IT Navigator works with two different AI coding assistants. Choose whichever you have access to:

- **VS Code + GitHub Copilot** (recommended for students with GitHub Education) -- see `QUICKSTART-COPILOT.md` for setup and usage instructions.
- **Claude Code** (alternative for students with Claude Pro) -- see `QUICKSTART-CLAUDE-CODE.md` for setup and usage instructions.

Both paths provide the same executive personas, rubrics, and evaluation capabilities. The difference is in how you interact with them.

## Enterprise IT Primer

The simulation is grounded in the [Enterprise IT Primer](https://leifulstrup.github.io/enterprise-it-primer/). The `primer/` directory in this repository contains 16 reference sections covering the full breadth of enterprise IT topics, plus consolidated industry judge advice:

| # | Section | Key Topics |
|---|---------|------------|
| 01 | IT Governance Frameworks | COBIT, ITIL, decision rights, governance structures |
| 02 | C-Suite IT Roles | CIO, CTO, CISO, CDO roles and responsibilities |
| 03 | IT Budgeting and Finance | Run/Grow/Transform, CapEx vs. OpEx, IT cost structures |
| 04 | Build vs. Buy vs. Subscribe | Sourcing decisions, evaluation criteria, trade-offs |
| 05 | Cloud Computing | IaaS, PaaS, SaaS, deployment models, shared responsibility |
| 06 | Enterprise Applications | ERP, CRM, SCM, integration patterns |
| 07 | Open Source Software | OSS licensing, community models, enterprise adoption |
| 08 | Cybersecurity Governance | NIST CSF, threat modeling, zero trust, incident response |
| 09 | Data Governance | Data quality, stewardship, privacy, master data management |
| 10 | Shadow IT | Risks, detection, governance approaches |
| 11 | Digital Transformation | Transformation strategy, maturity models, success factors |
| 12 | AI and Emerging Technology | AI/ML, blockchain, IoT, technology readiness levels |
| 13 | Innovation Management | Innovation pipelines, experimentation, scaling |
| 14 | Vendor Management | Kraljic Matrix, SLAs, contract negotiation, vendor risk |
| 15 | Project Management | Agile, Waterfall, hybrid, project governance |
| 16 | Industry Judge Advice | 10 recurring themes from 4 years of judge feedback (2021-2024) |

Executive personas will reference specific frameworks from these sections and weave in insights from past industry judges. Studying the primer before consulting with executives will help you engage more effectively and give stronger answers.

## Tips for Success

**Be specific.** Vague statements like "we will improve efficiency" or "this will reduce costs" will get immediate pushback from the executives. Use numbers, percentages, timeframes, and concrete examples. If you say "significant cost savings," the CFO will ask "how much, exactly?"

**Use frameworks from the primer.** Executives respond well when you demonstrate fluency with analytical frameworks. Reference the Kraljic Matrix when discussing vendor strategy, apply Kotter's 8-step model for change management, use NIST CSF for your security assessment, and cite Technology Readiness Levels when evaluating technology maturity.

**Prepare financial numbers.** Every proposal needs an ROI calculation, total cost of ownership (TCO) analysis, and payback period -- with clearly stated assumptions. The CFO will scrutinize every number, so know your sources and be ready to defend your estimates.

**Think about security and compliance from the start.** Do not treat cybersecurity, privacy, and regulatory compliance as an afterthought or a slide you add at the end. The CISO and General Counsel will test whether you have genuinely considered threats, privacy requirements (GDPR, CCPA, HIPAA), and applicable regulations.

**Have a real change management plan.** "We will train people" is not a change management plan. Identify affected stakeholders, assess organizational readiness, design a communication strategy, and plan for resistance. The CHRO will push you on this.

**Know your vendor strategy and exit plan.** If you are proposing a vendor solution, be ready to explain how you evaluated alternatives, what your lock-in mitigation strategy is, what SLAs you would negotiate, and what happens when the contract ends.

**Practice your 10-minute presentation timing.** Ten minutes goes by quickly. Know exactly what you need to cover on each slide and practice transitions. Cut anything that does not directly support your argument.

**Prepare for tough Q&A questions.** The industry judges will have 2-3 minutes to ask questions after your presentation. The executive personas in this simulation will help you anticipate exactly what those questions will be -- and practice answering them under pressure.

**Update your project brief as you learn.** Your brief is a living document. After each persona consultation, go back and update sections that need strengthening. The executives can only challenge what you have written down.

**Run link validation as a quality check.** If you move or rename files, run `uv run scripts/validate_markdown_links.py --root .` to catch any broken internal links before sharing your work.

**Start early and iterate.** Teams that use the simulation once the week before the presentation get limited benefit. Teams that start early, iterate multiple times, and systematically address gaps achieve the strongest results.
