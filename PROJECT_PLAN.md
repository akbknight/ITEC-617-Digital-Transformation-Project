# Project Plan — ITEC-617 Digital Transformation Simulation Coach

## Objective

Build an AI-powered simulation framework that lets MBA students practice defending digital transformation proposals against realistic challenge from nine executive personas. The simulation is grounded in four years of actual industry judge feedback (2021–2024) and the Enterprise IT Primer curriculum, producing domain-specific pressure that peer practice cannot replicate.

---

## Scope

### In Scope
- Nine executive personas (CIO, CFO, CISO, COO, CHRO, CDO, CMO, CPO, Board Director)
- Claude Code skill implementation (`.claude/skills/<role>/SKILL.md`)
- GitHub Copilot agent implementation (`.github/agents/<role>.agent.md`)
- Evaluation skill scoring proposals against 9 rubric categories, 45 criteria
- 16-module Enterprise IT Primer as grounding reference material
- Progress tracker for session-over-session improvement

### Out of Scope
- Deployed web application
- Persistent user accounts or cross-device sessions
- Real-time multi-player team simulation

---

## Architecture

The simulation has no backend, no database, and no deployed service. All logic runs inside the LLM context window, initialized by role-specific SKILL.md files. Students clone the repository and invoke personas directly from their editor via `/cio`, `/cfo`, etc. (Claude Code) or `@cio`, `@cfo`, etc. (GitHub Copilot Chat).

---

## Execution Phases

### Phase 1 — Persona Implementation (Complete)
- [x] Nine executive personas with domain-specific challenge patterns
- [x] Scoring guidance grounded in actual judge feedback
- [x] Primer references aligned with persona domain knowledge

### Phase 2 — Evaluation Framework (Complete)
- [x] Nine rubric categories: Business Case, Technology Selection, Financial Analysis, Risk and Security, Implementation Strategy, Change Management, Data and Analytics, Vendor Strategy, Presentation Readiness
- [x] 45 criteria mapped to industry judge evaluation standards
- [x] `evaluate` and `tracker` utility skills

### Phase 3 — Dual-Mode Support (Complete)
- [x] Claude Code skills in `.claude/skills/`
- [x] GitHub Copilot agents in `.github/agents/`
- [x] QUICKSTART guides for both modes

### Phase 4 — Documentation Upgrade (Complete)
- [x] `docs/methodology.md` — simulation design, persona grounding, evaluation framework
- [x] `docs/architecture.md` — component diagram, data flow, extensibility
- [x] `docs/decision_log.md` — six key design decisions with rationale

---

## Success Criteria

- [x] All nine personas implemented with domain-specific challenge patterns
- [x] Evaluation rubric grounded in industry judge criteria, not generic frameworks
- [x] Dual Claude Code + GitHub Copilot support
- [x] Primer references create direct alignment between study material and challenge questions
- [x] Documentation explains the system to a non-developer instructor
- [x] No AI-generated residue in any file
