# Architecture — ITEC-617 DT Simulation Coach

## System Overview

The simulation is a skill-based AI agent framework built on top of Claude Code and GitHub Copilot. It has no backend, no database, and no deployed service — all logic runs inside the LLM context window, initialized by role-specific SKILL.md files.

```
Student Workspace (git clone)
    │
    ├── .claude/skills/          ← Claude Code persona skills
    │   ├── cio/SKILL.md
    │   ├── cfo/SKILL.md
    │   ├── ciso/SKILL.md
    │   └── ... (9 personas + 4 utilities)
    │
    ├── .github/agents/          ← GitHub Copilot persona agents
    │   ├── cio.agent.md
    │   ├── cfo.agent.md
    │   └── ... (9 personas)
    │
    ├── primer/                  ← 16 domain knowledge modules
    │   ├── 01-it-governance-frameworks.md
    │   └── ...
    │
    ├── rubrics/                 ← 9 evaluation rubric files
    │   ├── 01-business-case.md
    │   └── ...
    │
    └── [student's proposal content]
```

---

## Component Architecture

### Persona Skills (`.claude/skills/<role>/SKILL.md`)

Each skill file instructs Claude Code to adopt a specific executive persona. When a student runs `/cio` in Claude Code:

1. Claude Code loads `.claude/skills/cio/SKILL.md` as the active instruction context
2. The SKILL.md establishes: persona name, role, domain expertise, evaluation priorities, question patterns
3. The persona then reads the student's proposal files from the workspace (via Claude Code's file access)
4. Challenges are grounded in both the persona's domain expertise and the relevant rubric dimension

### Evaluation Engine (`.claude/skills/evaluate/SKILL.md`)

The `evaluate` skill provides comprehensive multi-dimension scoring:
- Loads all 9 rubric files from `rubrics/`
- Assesses proposal against each of 45 criteria
- Returns dimension scores, identified gaps, and prioritized improvement recommendations

### Progress Tracking

Session-over-session improvement tracked by the `evaluate` skill comparing scores across evaluation runs. Students can observe convergence toward target scores across dimensions.

### Primer Context

Primer documents (`primer/`) provide grounding reference material. Personas are designed to probe students specifically on topics covered in the primer, creating alignment between study material and challenge questions.

---

## Dual-Mode Support

| Feature | Claude Code Mode | GitHub Copilot Mode |
|---------|-----------------|---------------------|
| Invocation | `/cio`, `/cfo`, etc. | `@cio`, `@cfo`, etc. in Copilot Chat |
| Skill files | `.claude/skills/<role>/SKILL.md` | `.github/agents/<role>.agent.md` |
| File access | Full workspace via Claude Code | Copilot Chat context window |
| Evaluation | `/evaluate` skill | `@evaluate` agent |
| Progress tracking | Tracked in session | Per-conversation |

---

## Data Flow

```
Student runs: /cio  (or @cio in Copilot)
      │
      ▼
Skill/Agent loads persona context
      │
      ▼
Persona reads student's proposal files in workspace
      │
      ▼
Persona generates challenge questions for 3-5 priority areas
      │
      ▼
Student responds → Persona provides coaching and follow-up
      │
      ▼
Student requests evaluation: /evaluate
      │
      ▼
Evaluate skill loads all 9 rubric files
      │
      ▼
Returns: dimension scores (1-5), gaps, top 3 improvement priorities
```

---

## Extensibility

New personas can be added by:
1. Creating `.claude/skills/<role>/SKILL.md` with the persona definition
2. Creating `.github/agents/<role>.agent.md` with equivalent instructions
3. Adding evaluation criteria to the relevant rubric file in `rubrics/`

The framework intentionally uses Markdown files rather than code, making it accessible to non-developers who want to add domain expertise.
