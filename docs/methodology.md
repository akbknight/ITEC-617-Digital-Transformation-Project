# Methodology — ITEC-617 DT Simulation Coach

## Problem Statement

MBA students preparing digital transformation presentations face a preparation gap: they can rehearse content, but they cannot rehearse challenge from domain experts in a realistic, personalized way. Industry judges at pitch competitions and internal reviewers at consulting firms evaluate proposals from highly specific perspectives (financial rigor, cybersecurity risk, change management readiness) that students rarely encounter during peer practice.

This simulation bridges that gap by instantiating nine executive personas that interrogate proposals from each domain perspective, backed by four years of actual industry judge feedback.

---

## Simulation Design Principles

### 1. Persona Grounding

Each persona is grounded in three sources:
1. **Role-specific domain knowledge** — CIO asks about enterprise architecture and IT governance frameworks; CFO asks about TCO analysis and NPV calculations; CISO asks about threat models and compliance requirements
2. **4 years of industry judge feedback (2021-2024)** — recurring patterns in what judges actually penalize (weak change management plans, missing security analysis, unrealistic ROI timelines)
3. **Enterprise IT Primer content** — 16 modules covering IT governance, cybersecurity, data strategy, vendor management, etc., ensuring persona questions align with course curriculum

### 2. Evaluation Framework

Rubric dimensions (9 categories, 45 criteria total) map to what industry judges actually evaluate:
- Business Case (financial justification, problem definition)
- Technology Selection (build vs. buy, vendor evaluation)
- Financial Analysis (TCO, NPV, payback period)
- Risk and Security (threat assessment, compliance, contingency)
- Implementation Strategy (timeline, milestones, pilot design)
- Change Management (stakeholder analysis, training, communication)
- Data and Analytics (data strategy, privacy, governance)
- Vendor Strategy (RFP process, negotiation, lock-in risk)
- Presentation Readiness (clarity, Q&A handling, executive communication)

### 3. Iterative Improvement Loop

The simulation enables tracked improvement across multiple sessions:
1. Student presents proposal to a persona
2. Persona challenges weak areas with specific, scored questions
3. Student refines proposal based on feedback
4. Next session with same or different persona reveals whether gaps were closed

Progress tracking (via `tracker/` module in Claude Code version) captures dimension-level scores across sessions, enabling the system to focus challenge prompts on consistently weak areas.

### 4. Dual-Mode Design

The project supports two interaction modes:
- **Claude Code mode**: Full persona skill library in `.claude/skills/`; students run from terminal with `claude /cio`, `/cfo`, etc.
- **GitHub Copilot mode**: Equivalent agents in `.github/agents/`; students use Copilot Chat with `@cio`, `@cfo`, etc.

This dual-mode design maximizes accessibility — students use whichever AI assistant their institution provides.

---

## Persona Implementation

Each persona is a Claude Code skill (SKILL.md file) containing:
- **Role context**: detailed description of the executive's priorities, concerns, and decision-making criteria
- **Domain knowledge**: specific frameworks and metrics the persona references (e.g., CFO references DCF analysis, IRR, and capital budgeting principles)
- **Challenge patterns**: specific types of questions derived from judge feedback
- **Scoring guidance**: how the persona evaluates responses across relevant rubric dimensions

Personas are designed to be appropriately skeptical but constructive — they do not simply reject proposals, they identify the weakest link in the argument and probe it systematically.

---

## Data Sources

- **Industry judge feedback**: 4 years (2021-2024) of ITEC-617 competition judge comments, anonymized and synthesized into recurring themes
- **Enterprise IT Primer**: Course content developed by Leif Ulstrup, covering 16 enterprise IT domains
- **Role-specific standards**: ISACA COBIT (governance), NIST CSF (security), PMI PMBOK (implementation), SHRM change management frameworks

---

## Limitations

1. **Persona consistency**: LLM responses are non-deterministic; the same question may receive different treatment across sessions. This is a feature for realistic practice but a limitation for objective assessment.
2. **Domain depth vs. breadth**: Each persona covers its domain at consulting-generalist depth, not practitioner depth. A real CISO would probe specific regulatory compliance requirements; the CISO persona approximates this.
3. **Scoring subjectivity**: Rubric scores are LLM judgments, not calibrated human evaluations. Use as directional guidance, not absolute benchmarks.
4. **No team dynamics simulation**: Current design is individual student ↔ persona; it does not simulate multi-presenter team dynamics.
