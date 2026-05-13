# Decision Log — ITEC-617 DT Simulation Coach

## Decision 1: Skill-based architecture over a deployed application

**Decision:** Use Claude Code skills and GitHub Copilot agents rather than building a deployed web application.

**Rationale:** MBA students preparing presentations have unpredictable schedules. A deployed app introduces availability, authentication, and cost complexity. Skills/agents run locally in the student's editor with no account required (beyond their existing Claude Code or Copilot access). This eliminates the single largest adoption barrier for a course tool.

**Tradeoff:** Less polished UX than a dedicated app; no persistent user accounts; no cross-device session continuity.

---

## Decision 2: Nine personas over a generalized "executive reviewer"

**Decision:** Implement nine distinct executive personas rather than one general executive reviewer.

**Rationale:** Domain-specific challenges produce more realistic preparation. A CFO's challenge set (NPV, IRR, payback period, capital budgeting) is fundamentally different from a CISO's challenge set (threat models, attack surface, compliance requirements). Collapsing these into one persona produces generic feedback that does not prepare students for specialized Q&A from domain experts.

**Evidence:** Four years of judge feedback showed that teams consistently failed on domain-specific questions they were unprepared for, particularly from the CISO, CFO, and CHRO perspectives.

---

## Decision 3: Markdown skill files over programmatic configuration

**Decision:** Each persona is defined in a Markdown SKILL.md file, not in JSON or YAML configuration or application code.

**Rationale:** Markdown is human-readable and editable by instructors without programming knowledge. It enables easy customization — an instructor can update the CFO persona's priorities to reflect current course content without touching any code. It also aligns naturally with how LLMs are instructed.

---

## Decision 4: Rubric alignment with industry judge criteria

**Decision:** Build rubric dimensions from 4 years of actual judge feedback rather than from academic literature alone.

**Rationale:** Students are evaluated by industry practitioners, not academics. Academic rubrics emphasize theoretical rigor; industry judges emphasize practical implementability, risk awareness, and executive communication clarity. The rubric is calibrated to what judges actually penalize, which differs meaningfully from generic "presentation quality" frameworks.

---

## Decision 5: Dual Claude Code + GitHub Copilot support

**Decision:** Maintain parallel implementations for Claude Code skills and GitHub Copilot agents.

**Rationale:** Different institutions and individual students have different AI tool access. Building both ensures no student is excluded due to tool availability. The implementation overhead is manageable because the underlying persona definitions (Markdown) are largely portable between the two formats.

---

## Decision 6: Reference to public Enterprise IT Primer

**Decision:** Ground all personas in the public Enterprise IT Primer (leifulstrup.github.io/enterprise-it-primer/) rather than custom course materials.

**Rationale:** The Primer is openly available, so students can read the exact material that grounds the persona's expertise. This creates a direct feedback loop: if the CIO persona probes IT governance, the student can read the governance primer module to understand the underlying framework. Custom course materials would create a closed loop that reduces independent learning.
