# Business Summaries — Staging Area for Team OneDrive

*Team: Signals>Noise | Course: ITEC-617 Information and Technology*

---

## Purpose

This folder is the **staging area for non-technical team members**. Every time technical content (Python/R code, data analysis, complex research) is generated in this project, the AI automatically produces a plain-English "Business Value Summary" and saves it here.

**Workflow:**
1. AI generates technical output (code, analysis, research) → AI also saves a Business Value Summary here
2. You copy files from this folder to the team's **OneDrive** shared folder for review by non-technical teammates
3. Non-technical teammates (Telecom Specialist, International Business Developer, Financial Analyst) can read, comment, and contribute without needing to understand the technical details

---

## File Naming Convention

Business Value Summary files follow this naming pattern:

```
YYYY-MM-DD_[topic-slug]_business-summary.md
```

**Examples:**
- `2026-03-21_roi-model-v1_business-summary.md`
- `2026-03-21_competitor-analysis_business-summary.md`
- `2026-04-01_pricing-algorithm_business-summary.md`

---

## Business Value Summary Template

When the AI creates a Business Value Summary, it uses this structure:

---

### Business Value Summary: [Topic]

**Date**: [Date]
**Prepared by**: AI Assistant (reviewed by [Team Member])
**Technical Source**: [Link or reference to technical document]

#### What We Did (Plain English)
[2-3 sentences explaining what was built or analyzed, in plain business language — no jargon]

#### Why It Matters to Our Business Case
[2-3 sentences on strategic relevance and connection to the DT project proposal]

#### Key Business Value
- **ROI Impact**: [How does this affect our financial projections?]
- **Strategic Value**: [How does this strengthen our competitive position or address the business problem?]
- **Risk Implication**: [Does this raise or reduce key risks?]

#### What This Means for Our Presentation
[1-2 sentences on how this finding should be reflected in our judge presentation]

#### Action Items for Team
| Teammate | Action | Due |
|---------|--------|-----|
| [IT Expert] | [Technical follow-up] | [Date] |
| [Telecom Specialist] | [Domain input needed] | [Date] |
| [Intl Business Developer] | [Market context to add] | [Date] |
| [Financial Analyst] | [Numbers to validate] | [Date] |

#### Questions for Persona Consultation
- [Question for `/cfo` regarding financials]
- [Question for `/cto` regarding technology]
- [Question for `/coo` regarding implementation]

---

## Contents of This Folder

| File | Topic | Date | Status |
|------|-------|------|--------|
| *(summaries will be added here as the project progresses)* | | | |

---

## OneDrive Sync Instructions

1. In Claude Code, navigate to this `documentation/business-summaries/` folder
2. Copy any file you want to share → paste into the team OneDrive folder
3. Notify teammates via the team channel
4. Note: do **not** sync the entire repository to OneDrive — only copy specific summary files

---

*To generate a Business Value Summary for any technical content, run `/business-summary` in Claude Code.*
